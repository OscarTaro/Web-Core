class LegalChatbot:
    def __init__(self):
        self.knowledge_base = self.load_knowledge_base()
    
    def load_knowledge_base(self):
        return {
            "rights": {
                "arrest": "When arrested in Zimbabwe, you have constitutional rights under Section 50: remain silent, legal representation, be informed of charges, medical treatment, protection from torture. Police must follow Criminal Procedure and Evidence Act.",
                "police": "Police powers are regulated by Police Act [Chapter 11:10]. You can request officer identification, know detention reasons, and report misconduct to Police General Headquarters (0242-700171).",
                "women_children": "Special protections under Domestic Violence Act [Chapter 5:16] and Maintenance Act [Chapter 5:09]. Gender Commission handles discrimination complaints.",
                "property": "Property rights protected under Constitution Section 71. For disputes, consult Deeds Registry or High Court depending on nature."
            },
            "court_process": {
                "filing": "Court filing requires: completed forms, filing fees (waivable for indigents), supporting affidavits. Magistrate Court handles cases up to $10,000, High Court for larger amounts.",
                "small_claims": "Small Claims Court (SCC) handles civil claims up to $5,000. No lawyers needed. Faster process - typically 30-60 days. Forms available at all magistrates courts.",
                "criminal": "Criminal process: arrest → initial remand → trial → sentencing. Bail applications possible at remand stage. Legal aid available for serious offenses.",
                "appeals": "Appeals go to High Court (from Magistrate) or Supreme Court (from High Court). 30-day deadline for most appeals."
            },
            "organizations": {
                "connectaid": "ConnectAid is a Zimbabwean legal empowerment platform founded to bridge justice gaps. We provide free legal information, referrals, and educational resources. Our mission: 'Justice Through Community Support'.",
                "angel_of_hope": "Angel of Hope Foundation (angelofhopezim.org) - Founded by First Lady Auxillia Mnangagwa. Focus: vulnerable children, women empowerment, health services. Contact: (024) 2709934. Programs: education support, menstrual health, food security.",
                "legal_resources_foundation": "LRF (lrfzim.com) - Established 1985. Provides legal aid, education, law reform advocacy. Offices in Harare, Bulawayo, Gweru. Free services for qualifying individuals.",
                "human_rights_ngo_forum": "Zimbabwe Human Rights NGO Forum (hrforumzim.org) - Coalition of 21 human rights organizations. Documents violations, provides legal assistance, advocacy. Known for human rights reports.",
                "childline_zimbabwe": "Childline (childline.org.zw) - Child protection organization. 24/7 toll-free: 116. Services: counseling, legal aid for children, abuse response. Established 1998.",
                "zhrc": "Zimbabwe Human Rights Commission (zhrc.org.zw) - Constitutional body investigating rights violations. Complaints: online, phone, or office visits. Powers to summon witnesses.",
                "adult_rape_clinic": "Adult Rape Clinic (adultrapeclinic.org) - Medical, legal, psychological support for sexual violence survivors. Forensic evidence collection, court preparation, counseling.",
                "justice_for_children": "Justice for Children - Specializes in juvenile justice. Legal representation for children in conflict with law. Child-friendly legal processes.",
                "habakkuk_trust": "Habakkuk Trust (habakkuktrust.org) - Community mobilization for rights. Focus: marginalized communities, governance advocacy. Based in Bulawayo."
            },
            "resources": {
                "affidavit": "Affidavit requirements: Commissioner of Oaths stamp, full names, ID number, physical address, clear facts. Download templates from our Resources section.",
                "constitution": "Zimbabwe Constitution (2021 Amendment) available for download. Key chapters: Declaration of Rights (4), Citizenship (3), Executive (5).",
                "legal_aid": "Free legal aid providers: Legal Resources Foundation, Zimbabwe Lawyers for Human Rights, University of Zimbabwe Legal Aid Clinic. Means test applies.",
                "emergency_contacts": "Immediate help: Police VFU (0242 744 785), Medical Emergency (MARS 0741 800 800), Legal Resources Foundation (0242 708 708).",
                "gbv_resources": "GBV support: Musasa Project (08080074), Adult Rape Clinic, ZRP Victim Friendly Unit. Protection orders available under Domestic Violence Act."
            },
            "procedures": {
                "protection_order": "Domestic Violence Protection Order: Apply at Magistrate Court. Emergency orders granted within 24 hours. Free for survivors.",
                "maintenance_claim": "Maintenance claims: File at Maintenance Court. Evidence required: income proof, child expenses. Enforcement through garnishee orders.",
                "eviction_process": "Eviction legality: Court order required. Illegal evictions report to police. Alternative accommodation may be ordered.",
                "employment_disputes": "Labor issues: NEC for specific sectors, Labor Court for appeals. Unfair dismissal claims within 6 months."
            },
            "website_info": {
                "founder": "ConnectAid was established by legal professionals and community advocates to address justice accessibility gaps in Zimbabwe.",
                "services": "We provide: legal education, organization referrals, downloadable resources, multi-language support, emergency contact information.",
                "languages": "Available languages: English, Shona, Ndebele, Shivenda. Language justice is central to our accessibility approach.",
                "privacy": "We prioritize user privacy. No personal data stored without consent. Secure reporting channels with encryption."
            }
        }
    
    def find_answer(self, question):
        if not question or not question.strip():
            return "Please ask a question about Zimbabwean law, legal rights, or our services."
            
        question_lower = question.lower().strip()
        
        # Enhanced matching with better keyword detection
        keywords = question_lower.split()
        
        # Legal rights - more specific matching
        if any(word in question_lower for word in ['arrest', 'arrested', 'detain', 'detention']):
            return self.knowledge_base["rights"]["arrest"]
        elif any(word in question_lower for word in ['police', 'officer', 'law enforcement']):
            return self.knowledge_base["rights"]["police"]
        elif any(word in question_lower for word in ['women', 'child', 'children', 'gender', 'domestic']):
            return self.knowledge_base["rights"]["women_children"]
        elif any(word in question_lower for word in ['property', 'land', 'house']):
            return self.knowledge_base["rights"]["property"]
        
        # Court processes
        elif any(word in question_lower for word in ['file', 'filing', 'sue', 'lawsuit']):
            return self.knowledge_base["court_process"]["filing"]
        elif any(word in question_lower for word in ['small claim', 'small court', 'small claims']):
            return self.knowledge_base["court_process"]["small_claims"]
        elif any(word in question_lower for word in ['criminal', 'crime', 'offense']):
            return self.knowledge_base["court_process"]["criminal"]
        elif 'appeal' in question_lower:
            return self.knowledge_base["court_process"]["appeals"]
        
        # Organizations - more flexible matching
        elif 'angel' in question_lower and 'hope' in question_lower:
            return self.knowledge_base["organizations"]["angel_of_hope"]
        elif any(word in question_lower for word in ['lrf', 'legal resources', 'legal foundation']):
            return self.knowledge_base["organizations"]["legal_resources_foundation"]
        elif any(word in question_lower for word in ['human rights forum', 'ngo forum']):
            return self.knowledge_base["organizations"]["human_rights_ngo_forum"]
        elif any(word in question_lower for word in ['childline', 'child line']):
            return self.knowledge_base["organizations"]["childline_zimbabwe"]
        elif any(word in question_lower for word in ['human rights commission', 'zhrc']):
            return self.knowledge_base["organizations"]["zhrc"]
        elif any(word in question_lower for word in ['rape clinic', 'adult rape', 'sexual violence']):
            return self.knowledge_base["organizations"]["adult_rape_clinic"]
        elif 'justice for children' in question_lower:
            return self.knowledge_base["organizations"]["justice_for_children"]
        elif 'habakkuk' in question_lower:
            return self.knowledge_base["organizations"]["habakkuk_trust"]
        elif any(word in question_lower for word in ['connectaid', 'this website', 'who are you', 'what is this']):
            return self.knowledge_base["organizations"]["connectaid"]
        
        # Resources
        elif any(word in question_lower for word in ['affidavit', 'sworn statement']):
            return self.knowledge_base["resources"]["affidavit"]
        elif 'constitution' in question_lower:
            return self.knowledge_base["resources"]["constitution"]
        elif any(word in question_lower for word in ['legal aid', 'free lawyer', 'pro bono']):
            return self.knowledge_base["resources"]["legal_aid"]
        elif any(word in question_lower for word in ['emergency', 'urgent', 'help now']):
            return self.knowledge_base["resources"]["emergency_contacts"]
        elif any(word in question_lower for word in ['gbv', 'gender violence', 'domestic violence']):
            return self.knowledge_base["resources"]["gbv_resources"]
        
        # Procedures
        elif any(word in question_lower for word in ['protection order', 'restraining order']):
            return self.knowledge_base["procedures"]["protection_order"]
        elif 'maintenance' in question_lower:
            return self.knowledge_base["procedures"]["maintenance_claim"]
        elif any(word in question_lower for word in ['eviction', 'evict']):
            return self.knowledge_base["procedures"]["eviction_process"]
        elif any(word in question_lower for word in ['employment', 'labour', 'dismissal', 'job']):
            return self.knowledge_base["procedures"]["employment_disputes"]
        
        # Website information
        elif any(word in question_lower for word in ['founder', 'who started', 'established']):
            return self.knowledge_base["website_info"]["founder"]
        elif any(word in question_lower for word in ['service', 'what do you provide', 'what do you do']):
            return self.knowledge_base["website_info"]["services"]
        elif any(word in question_lower for word in ['language', 'shona', 'ndebele', 'shivenda']):
            return self.knowledge_base["website_info"]["languages"]
        elif any(word in question_lower for word in ['privacy', 'data protection', 'confidential']):
            return self.knowledge_base["website_info"]["privacy"]
        
        # Default response with better guidance
        else:
            return "I can help you with information about: Legal rights in Zimbabwe, court processes, our partner organizations (Angel of Hope, LRF, Childline, etc.), legal procedures, and ConnectAid services. Please try asking about a specific topic like 'What is Angel of Hope Foundation?' or 'How do I file a small claims case?'"