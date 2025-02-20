import os
import random
import json
import struct

def ensure_files_directory():
    """Create the files directory if it doesn't exist"""
    os.makedirs('files', exist_ok=True)

def generate_banking_app():
    """Generate a simplified version of the banking app source code"""
    app_content = """
    # Vulnerable Banking Application
    # Contains intentional vulnerabilities in OAuth implementation
    # and API endpoint security
    
    class BankingApp:
        def __init__(self):
            self.oauth_config = {
                "client_id": "REDACTED",
                "client_secret": "REDACTED",
                "redirect_uri": "http://bank.local/callback"
            }
            
        def process_oauth_callback(self, code):
            # Vulnerable OAuth implementation
            # TODO: Fix CSRF vulnerability
            pass
            
        def verify_jwt(self, token):
            # Vulnerable JWT verification
            # Missing algorithm verification
            pass
            
        def process_transaction(self, user_id, amount):
            # Vulnerable transaction processing
            # Missing proper authorization checks
            pass
    """
    
    with open('files/banking_app.zip', 'w') as f:
        f.write(app_content)

def generate_crypto_challenge():
    """Generate the cryptographic challenge files"""
    # Create a simplified version of the crypto implementation
    crypto_impl = """
    class QuantumSafeEncryption:
        def __init__(self):
            self.lattice_params = self.generate_lattice_params()
            self.zero_knowledge_params = self.generate_zk_params()
            
        def generate_lattice_params(self):
            # Vulnerable lattice parameter generation
            # Contains implementation flaw
            pass
            
        def encrypt(self, message):
            # Vulnerable encryption implementation
            pass
            
        def generate_proof(self):
            # Vulnerable zero-knowledge proof generation
            pass
    """
    
    with open('files/crypto_implementation.py', 'w') as f:
        f.write(crypto_impl)
    
    # Generate public parameters
    params = {
        "lattice_dimension": 512,
        "q": 12289,
        "error_distribution": "discrete_gaussian",
        "public_key": "REDACTED"
    }
    
    with open('files/public_parameters.json', 'w') as f:
        json.dump(params, f, indent=4)

def generate_hardware_challenge():
    """Generate the hardware challenge firmware"""
    # Create a simple firmware binary with embedded flag
    firmware = bytearray([
        0x7F, 0x45, 0x4C, 0x46,  # ELF magic number
        # ... more binary content ...
    ])
    
    with open('files/firmware.bin', 'wb') as f:
        f.write(firmware)

def main():
    ensure_files_directory()
    
    # Generate all challenge files
    generate_banking_app()
    generate_crypto_challenge()
    generate_hardware_challenge()
    
    print("Generated challenge files in the files/ directory")

if __name__ == "__main__":
    main() 