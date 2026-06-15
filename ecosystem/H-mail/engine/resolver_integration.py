from ecosystem.DNSMeshResolver.resolver import resolver

def resolve_hmail_recipient(address):
    # If it ends in .Huma, use our custom DNS-Mesh resolver
    if address.endswith(".Huma"):
        return resolver.resolve(address)
    return "External_SMTP_Gateway"
