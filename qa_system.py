import os
from datetime import datetime, timedelta
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from models.resort import Resort
from models.user import User
from models.booking import Booking
from extensions import db
from dateutil.parser import parse
import re

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = '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'

class Document:
    def __init__(self, content, metadata=None):
        self.page_content = content
        self.metadata = metadata if metadata is not None else {}

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def setup_qa_system():
    resorts = Resort.query.all()
    docs = [Document(content=f"{resort.name} (ID: {resort.id})\nLocation: {resort.location}\nAccess Level: {resort.access_level}") for resort in resorts]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    rag_chain = ({"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())

    return rag_chain

def handle_resort_suggestions(question):
    rag_chain = setup_qa_system()
    suggestions = rag_chain.invoke(question)
    return suggestions

def extract_resort_id(question):
    words = question.split()
    for word in words:
        if word.isdigit():
            return int(word)
    return None

def handle_user_details(question, user_id):
    user = User.query.get(user_id)
    if not user:
        return "User not found.", None, None

    # Example logic to extract a date from the question
    # Using regex and dateutil.parser for demonstration
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', question)
    check_in_date = parse(dates[0]).date() if dates else datetime.now().date()

    # Example logic to extract duration (in days) from the question
    duration_matches = re.findall(r'\b\d+\b', question)
    duration = int(duration_matches[0]) if duration_matches else 7  # Default to 7 days

    return f"User details for {user.username} are confirmed.", check_in_date, duration
def handle_booking(question, user_id, resort_id, check_in_date, duration):
    user = User.query.get(user_id)
    if not user:
        return "User not found."

    resort = Resort.query.get(resort_id)
    if not resort:
        return "Resort not found."

    # Check user's membership level against resort's access level
    if not is_membership_valid(user.membership_type, resort.access_level):
        return "Your membership level does not permit booking at this resort."

    check_out_date = check_in_date + timedelta(days=duration)
    new_booking = Booking(user_id=user_id, resort_id=resort_id, check_in_date=check_in_date, check_out_date=check_out_date)
    db.session.add(new_booking)
    db.session.commit()

    return f"Booking confirmed at {resort.name} from {check_in_date.strftime('%Y-%m-%d')} to {check_out_date.strftime('%Y-%m-%d')}."

def is_membership_valid(user_membership, resort_access_level):
    # Implement logic to check if user's membership level matches or exceeds the resort's access level
    # This is a simplified example
    membership_levels = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ascendant']
    user_index = membership_levels.index(user_membership)
    resort_index = membership_levels.index(resort_access_level)
    return user_index >= resort_index

def get_answer(question, user_id=None, stage='suggestion', context={}):
    if stage == 'suggestion':
        response = handle_resort_suggestions(question)
        return response, 'user_details', context
    elif stage == 'user_details':
        response, check_in_date, duration = handle_user_details(question, user_id)
        context.update({'check_in_date': check_in_date, 'duration': duration})
        return response, 'booking', context
    elif stage == 'booking':
        resort_id = extract_resort_id(question)
        check_in_date = context.get('check_in_date')
        duration = context.get('duration')
        response = handle_booking(question, user_id, resort_id, check_in_date, duration)
        return response, 'end', {}
    else:
        rag_chain = setup_qa_system()
        response = rag_chain.invoke(question)
        return response, stage, context
