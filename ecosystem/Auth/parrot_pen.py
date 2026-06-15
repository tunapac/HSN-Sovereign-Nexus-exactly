# Golden Parrot Feathers Pen: Cryptographic Signing Service
# Purpose: Non-repudiable identity signing for the Huma Ecosystem
import nacl.signing
import nacl.encoding

class ParrotPen:
    def __init__(self):
        # Generate a private key for the developer
        self.signing_key = nacl.signing.SigningKey.generate()
        self.verify_key = self.signing_key.verify_key
        
    def sign_message(self, message: str):
        # Apply the "Golden Feather" signature
        signed = self.signing_key.sign(message.encode())
        return signed

    def get_public_identity(self):
        return self.verify_key.encode(encoder=nacl.encoding.HexEncoder)

# Example usage for signing a new artifact
pen = ParrotPen()
print(f"Identity Registered: {pen.get_public_identity().decode()}")
