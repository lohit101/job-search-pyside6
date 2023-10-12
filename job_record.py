class JobRecord:
    def __init__(self, advert_type, status, date, company, position, link, ad_text, contact, notes, reminder_dates):
        self.advert_type = advert_type
        self.status = status
        self.date = date
        self.company = company
        self.position = position
        self.link = link
        self.ad_text = ad_text
        self.contact = contact
        self.notes = notes
        self.reminder_dates = reminder_dates
