def extract_certifications(text):

    certifications = []

    known_certs = [

        "AWS",

        "Oracle",

        "Cisco",

        "Salesforce",

        "Google",

        "Microsoft",

        "Azure",

        "IBM",

        "Coursera",

        "NPTEL"
    ]

    for cert in known_certs:

        if cert.lower() in text.lower():

            certifications.append(cert)

    return certifications