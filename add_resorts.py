from app import create_app
from models.resort import Resort
from extensions import db

app = create_app()


def add_resorts():
    with app.app_context():  # This line sets up the application context
        resorts = [
            {"name": "The Drake Hotel", "location": "Chicago, Illinois, USA",
             "accommodations": "Modern styled rooms, city views",
             "dining": "Restaurant, cafe, rooftop bar, room service",
             "fitness_wellness": "Spa, fitness center",
             "business_facilities": "Business center, conference facilities",
             "concierge_services": "Tours, bookings, and recommendations",
             "entertainment": "Proximity to Chicago's cultural venues, hosting regular events",
             "additional_services": "Valet parking, laundry, dry cleaning",
             "security": "24-hour surveillance",
             "access_level": "Gold and Platinum"},
            {"name": "Sunset Bay Resort", "location": "Maui, Hawaii, USA",
             "accommodations": "Beachfront villas, ocean views",
             "dining": "Seafood restaurant, poolside bar, in-room dining",
             "fitness_wellness": "Outdoor yoga studio, wellness spa",
             "business_facilities": "Meeting rooms with ocean view",
             "concierge_services": "Island tours, water sports bookings",
             "entertainment": "Beach parties, live music events",
             "additional_services": "Private beach access, jet ski rentals",
             "security": "Gated property, 24-hour security",
             "access_level": "Diamond and Ascendant"},
            {"name": "Mountain Escape Lodge", "location": "Aspen, Colorado, USA",
             "accommodations": "Luxury cabins, mountain views",
             "dining": "Gourmet restaurant, wine bar, outdoor grilling",
             "fitness_wellness": "Heated outdoor pools, full-service spa",
             "business_facilities": "High-tech meeting rooms, business lounge",
             "concierge_services": "Ski rentals, mountain tour bookings",
             "entertainment": "Evening bonfires, live jazz nights",
             "additional_services": "Ski-in/ski-out access, gear storage",
             "security": "24-hour on-site security personnel",
             "access_level": "Platinum and Diamond"},
            {"name": "Coral Reef Retreat", "location": "Bora Bora, French Polynesia",
             "accommodations": "Overwater bungalows with glass floors",
             "dining": "Exclusive underwater restaurant, beachside BBQ",
             "fitness_wellness": "Scuba diving center, holistic spa treatments",
             "business_facilities": "Seaside conference rooms with state-of-the-art technology",
             "concierge_services": "Personalized island tours, snorkeling excursions",
             "entertainment": "Traditional Polynesian fire dancing shows",
             "additional_services": "Private boat charters, helicopter tours",
             "security": "Discreet 24-hour security service",
             "access_level": "Diamond and Elite"},
            {"name": "Urban Oasis Hotel", "location": "New York City, New York, USA",
             "accommodations": "Luxurious suites with panoramic city views",
             "dining": "Michelin-starred restaurant, trendy rooftop lounge",
             "fitness_wellness": "High-end fitness center, in-room massage services",
             "business_facilities": "Executive business lounge, private meeting rooms",
             "concierge_services": "Broadway tickets, exclusive restaurant reservations",
             "entertainment": "Private gallery viewings, VIP club access",
             "additional_services": "Personal shopper, limousine service",
             "security": "Round-the-clock security and surveillance",
             "access_level": "Platinum and Elite"},
            {"name": "Safari Wilderness Lodge", "location": "Serengeti, Tanzania",
             "accommodations": "Eco-friendly tents with wild savannah views",
             "dining": "Open-air dining with authentic African cuisine",
             "fitness_wellness": "Guided yoga sessions overlooking the Serengeti",
             "business_facilities": "Outdoor conference spaces with natural lighting",
             "concierge_services": "Safari tours, cultural village visits",
             "entertainment": "Evening campfires with storytelling",
             "additional_services": "Wildlife photography workshops, hot air balloon rides",
             "security": "Trained wildlife guides and security staff",
             "access_level": "Gold and Platinum"},
            {"name": "Arctic Circle Resort", "location": "Rovaniemi, Finland",
             "accommodations": "Glass igloos under the Northern Lights",
             "dining": "Local Lappish cuisine, ice bar experience",
             "fitness_wellness": "Outdoor heated pools, traditional Finnish sauna",
             "business_facilities": "Ice meeting rooms, high-speed internet",
             "concierge_services": "Aurora hunting, husky sledding",
             "entertainment": "Ice sculpture workshops, Sami cultural shows",
             "additional_services": "Winter gear rental, heated transportation",
             "security": "24/7 on-call assistance",
             "access_level": "Diamond and Elite"},
            {"name": "Venetian Palace Resort", "location": "Venice, Italy",
             "accommodations": "Historic rooms with canal views, Venetian décor",
             "dining": "Gourmet Italian dining, exclusive wine cellar tours",
             "fitness_wellness": "Private gym, rooftop yoga overlooking Venice",
             "business_facilities": "Elegant meeting rooms with Renaissance art",
             "concierge_services": "Private gondola tours, art gallery visits",
             "entertainment": "Opera nights, Venetian mask-making classes",
             "additional_services": "Personal butler, luxury shopping guide",
             "security": "Personal security detail available upon request",
             "access_level": "Elite and Ascendant"},
            {"name": "Rainforest Haven Inn", "location": "Amazon Rainforest, Brazil",
             "accommodations": "Eco-friendly treehouses with rainforest canopy views",
             "dining": "Organic rainforest-to-table cuisine, jungle bar",
             "fitness_wellness": "Jungle trekking, river kayaking",
             "business_facilities": "Eco-friendly conference rooms with natural acoustics",
             "concierge_services": "Amazon river cruises, indigenous tribe encounters",
             "entertainment": "Night wildlife tours, Amazonian storytelling",
             "additional_services": "Rainforest conservation tours, birdwatching expeditions",
             "security": "Eco-trained security staff, emergency medical services",
             "access_level": "Gold and Platinum"},
           {"name": "Alpine Ski Haven", "location": "Zermatt, Switzerland",
            "accommodations": "Cozy chalets with mountain vistas",
            "dining": "Gourmet alpine cuisine, après-ski lounge",
            "fitness_wellness": "Indoor heated pool, full-service spa",
            "business_facilities": "High-altitude conference rooms with inspiring views",
            "concierge_services": "Ski pass arrangement, guided mountain tours",
            "entertainment": "Live alpine music, fondue nights",
            "additional_services": "Ski equipment hire, shuttle to ski lifts",
            "security": "24-hour onsite assistance",
            "access_level": "Platinum and Diamond"},
           {"name": "Tropical Paradise Resort", "location": "Maldives",
            "accommodations": "Private overwater villas with infinity pools",
            "dining": "Fresh seafood grill, sunset cocktails",
            "fitness_wellness": "Dive center, Ayurvedic spa treatments",
            "business_facilities": "Beachfront meeting spaces, high-speed Wi-Fi",
            "concierge_services": "Scuba diving excursions, romantic beach dinners",
            "entertainment": "Live tropical music, water sports",
            "additional_services": "Seaplane tours, personal butler service",
            "security": "Discrete security monitoring, medical staff on standby",
            "access_level": "Elite and Ascendant"},
           {"name": "Desert Mirage Resort", "location": "Dubai, United Arab Emirates",
            "accommodations": "Luxury suites with panoramic desert views",
            "dining": "Award-winning Arabic cuisine, rooftop terrace",
            "fitness_wellness": "Desert yoga, state-of-the-art fitness center",
            "business_facilities": "Advanced tech meeting rooms, business lounge",
            "concierge_services": "Desert safari, cultural experiences",
            "entertainment": "Belly dancing shows, camel rides",
            "additional_services": "Luxury car rentals, VIP shopping experiences",
            "security": "High-level security protocols",
            "access_level": "Gold and Platinum"},
           {"name": "Historic Castle Retreat", "location": "Edinburgh, Scotland",
            "accommodations": "Regal rooms in a historic castle",
            "dining": "Scottish gourmet dining, whiskey tasting bar",
            "fitness_wellness": "Countryside walks, wellness spa",
            "business_facilities": "Elegant ballrooms for meetings and events",
            "concierge_services": "Highland tours, historical excursions",
            "entertainment": "Bagpipe performances, medieval banquets",
            "additional_services": "Genealogy services, kilt fitting",
            "security": "24-hour surveillance, guest privacy prioritized",
            "access_level": "Diamond and Elite"},
           {"name": "Lakeside Wellness Retreat", "location": "Lake Como, Italy",
            "accommodations": "Elegant villas with lake views",
            "dining": "Italian lakeside dining, wine cellar",
            "fitness_wellness": "Outdoor yoga, thermal spa",
            "business_facilities": "Lakeview conference rooms, tech support",
            "concierge_services": "Boat trips, villa tours",
            "entertainment": "Open-air cinema, live music evenings",
            "additional_services": "Private jetty, limousine transfers",
            "security": "Discreet personal security on request",
            "access_level": "Platinum and Ascendant"},
           {"name": "Cliffside Ocean Resort", "location": "Santorini, Greece",
            "accommodations": "Whitewashed suites with caldera views",
            "dining": "Mediterranean fusion cuisine, cliffside dining",
            "fitness_wellness": "Infinity pools, wellness therapies",
            "business_facilities": "Terrace meeting areas, A/V equipment",
            "concierge_services": "Catamaran tours, archaeological site visits",
            "entertainment": "Greek nights, wine tasting tours",
            "additional_services": "Helicopter rides, private yacht charters",
            "security": "24/7 on-site personnel, guest confidentiality",
            "access_level": "Gold and Elite"},
           {"name": "Urban Zen Oasis", "location": "Tokyo, Japan",
            "accommodations": "Modern minimalist rooms with city skyline",
            "dining": "Japanese fusion cuisine, rooftop sushi bar",
            "fitness_wellness": "Zen meditation garden, luxury spa",
            "business_facilities": "High-tech meeting spaces, virtual conferencing",
            "concierge_services": "City tours, cultural experiences",
            "entertainment": "Live traditional music, tea ceremonies",
            "additional_services": "Personal shopper, translation services",
            "security": "Discreet surveillance, 24-hour guest assistance",
            "access_level": "Diamond and Elite"},
           {"name": "Rainforest Eco-Resort", "location": "Costa Rica",
            "accommodations": "Eco-friendly bungalows amidst rainforest",
            "dining": "Organic farm-to-table meals, jungle café",
            "fitness_wellness": "Yoga pavilion, natural thermal springs",
            "business_facilities": "Eco-conference rooms, green technology",
            "concierge_services": "Rainforest hikes, wildlife tours",
            "entertainment": "Local music nights, sustainability workshops",
            "additional_services": "Eco-tour guidance, adventure sports arrangements",
            "security": "Eco-friendly security measures, medical staff on-site",
            "access_level": "Gold and Platinum"},
           {"name": "Royal Raj Palace", "location": "Jaipur, India",
            "accommodations": "Opulent suites with traditional Rajasthani decor",
            "dining": "Royal Indian cuisine, Mughal-inspired courtyard dining",
            "fitness_wellness": "Palace yoga sessions, Ayurvedic spa",
            "business_facilities": "Majestic conference halls, business center",
            "concierge_services": "Elephant rides, heritage tours",
            "entertainment": "Folk dances, puppet shows",
            "additional_services": "Royal banquet arrangements, custom tours",
            "security": "Royal guard security, discreet surveillance",
            "access_level": "Elite and Ascendant"},
           {"name": "Arctic Wilderness Lodge", "location": "Reykjavik, Iceland",
            "accommodations": "Cozy lodges with aurora borealis views",
            "dining": "Nordic cuisine, ice bar",
            "fitness_wellness": "Geothermal hot springs, wilderness hikes",
            "business_facilities": "Scenic conference rooms, tech support",
            "concierge_services": "Glacier tours, northern lights expeditions",
            "entertainment": "Icelandic folklore evenings, outdoor adventures",
            "additional_services": "Private guides, photography tours",
            "security": "Remote location safety protocols",
            "access_level": "Platinum and Diamond"},
           {"name": "Savannah Safari Retreat", "location": "Kenya",
            "accommodations": "Luxury tents overlooking the savannah",
            "dining": "African fusion cuisine, sunset barbecues",
            "fitness_wellness": "Guided nature walks, wellness spa",
            "business_facilities": "Safari-themed meeting rooms, open-air lounges",
            "concierge_services": "Wildlife safaris, cultural village visits",
            "entertainment": "Traditional Maasai performances, star gazing",
            "additional_services": "Balloon safaris, photography workshops",
            "security": "Rangers on patrol, guest safety briefings",
            "access_level": "Elite and Ascendant"},
          {"name": "Lakeside Leisure Resort", "location": "Lake Tahoe, California, USA",
           "accommodations": "Rustic lakeside cabins with panoramic views",
           "dining": "Local cuisine, lakefront dining experience",
           "fitness_wellness": "Outdoor activities, wellness spa",
           "business_facilities": "Lake view meeting rooms, high-speed Wi-Fi",
           "concierge_services": "Boating, fishing trips",
           "entertainment": "Evening bonfires, live music by the lake",
           "additional_services": "Private dock access, water sports rentals",
           "security": "24-hour surveillance, guest services",
           "access_level": "Gold and Platinum"},

          {"name": "Coastal Charm Inn", "location": "Savannah, Georgia, USA",
           "accommodations": "Elegant rooms with Southern charm",
           "dining": "Gourmet Southern cuisine, rooftop terrace bar",
           "fitness_wellness": "Fitness center, in-room massages",
           "business_facilities": "Historic conference spaces, modern amenities",
           "concierge_services": "City tours, culinary experiences",
           "entertainment": "Jazz nights, art exhibitions",
           "additional_services": "Bicycle rentals, personal concierge",
           "security": "Discreet guest security, 24-hour front desk",
           "access_level": "Silver and Gold"},
          {"name": "Urban Retreat Tower", "location": "New York City, New York, USA",
           "accommodations": "Luxury suites with skyline views",
           "dining": "International cuisine, rooftop lounge",
           "fitness_wellness": "State-of-the-art gym, rooftop pool",
           "business_facilities": "High-tech business center, private meeting rooms",
           "concierge_services": "Broadway tickets, exclusive restaurant reservations",
           "entertainment": "Cocktail hours, city excursions",
           "additional_services": "Limousine service, personal shopping",
           "security": "High-end security systems, concierge",
           "access_level": "Platinum and Elite"},
          {"name": "Himalayan Hideaway", "location": "Manali, Himachal Pradesh, India",
           "accommodations": "Mountain view cottages with traditional decor",
           "dining": "Himachali cuisine, outdoor dining",
           "fitness_wellness": "Yoga retreats, natural hot springs",
           "business_facilities": "Conference rooms with mountain views",
           "concierge_services": "Trekking expeditions, cultural tours",
           "entertainment": "Local music and dance, campfire nights",
           "additional_services": "Adventure sports arrangements, travel desk",
           "security": "Round-the-clock security, emergency services",
           "access_level": "Gold and Platinum"},
          {"name": "Royal Heritage Palace", "location": "Udaipur, Rajasthan, India",
           "accommodations": "Luxurious suites in a heritage palace",
           "dining": "Royal Rajasthani feasts, lakeside dining",
           "fitness_wellness": "Palace spa, yoga sessions",
           "business_facilities": "Regal conference halls, modern amenities",
           "concierge_services": "Heritage walks, horse carriage rides",
           "entertainment": "Folk performances, puppet shows",
           "additional_services": "Private boat rides, cultural experiences",
           "security": "Royal guard, modern surveillance",
           "access_level": "Elite and Ascendant"}
        ]

        for resort_info in resorts:
            resort = Resort(**resort_info)
            db.session.add(resort)

        db.session.commit()


if __name__ == '__main__':
    add_resorts()
