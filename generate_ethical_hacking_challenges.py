import os
import yaml
import json
import base64

def ensure_files_directory():
    """Create the files directory if it doesn't exist"""
    os.makedirs('files', exist_ok=True)

def generate_network_pentest_files():
    """Generate files for the enterprise network penetration challenge"""
    # Create network diagram (simplified version)
    network_diagram = """
    Corporate Network Infrastructure
    ------------------------------
    DMZ -> Firewall -> Internal Network
          |-> AD DC (Primary)
          |-> File Servers
          |-> Database Servers
    """
    
    with open('files/network_diagram.pdf', 'w') as f:
        f.write(network_diagram)
    
    # Create VPN configuration
    vpn_config = """
    client
    dev tun
    proto udp
    remote vpn.challenge.local 1194
    resolv-retry infinite
    nobind
    persist-key
    persist-tun
    ca ca.crt
    cert client.crt
    key client.key
    remote-cert-tls server
    cipher AES-256-CBC
    verb 3
    """
    
    with open('files/vpn_config.ovpn', 'w') as f:
        f.write(vpn_config)

def generate_iot_challenge_files():
    """Generate files for the IoT exploitation challenge"""
    # Create device firmware (simplified)
    firmware = bytearray([
        0x7F, 0x45, 0x4C, 0x46,  # ELF magic number
        # Add more binary content here
    ])
    
    with open('files/device_firmware.bin', 'wb') as f:
        f.write(firmware)
    
    # Create protocol specifications
    protocol_specs = """
    MQTT Topics:
    - /building/hvac/status
    - /building/access/logs
    - /building/security/alerts
    
    CoAP Endpoints:
    - /api/v1/device/status
    - /api/v1/device/control
    """
    
    with open('files/protocol_specs.pdf', 'w') as f:
        f.write(protocol_specs)

def generate_cloud_challenge_files():
    """Generate files for the cloud infrastructure challenge"""
    # Create IAM policy
    iam_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetObject"
                ],
                "Resource": [
                    "arn:aws:s3:::challenge-bucket",
                    "arn:aws:s3:::challenge-bucket/*"
                ]
            }
        ]
    }
    
    with open('files/iam_policy.json', 'w') as f:
        json.dump(iam_policy, f, indent=4)
    
    # Create AWS credentials
    aws_credentials = """
    [default]
    aws_access_key_id = AKIA****************
    aws_secret_access_key = ****************************************
    region = us-west-2
    """
    
    with open('files/aws_credentials.txt', 'w') as f:
        f.write(aws_credentials)

def generate_supply_chain_files():
    """Generate files for the supply chain attack challenge"""
    # Create CI/CD pipeline configuration
    pipeline_config = """
    stages:
      - test
      - build
      - security_scan
      - deploy

    test:
      script:
        - run_tests.sh
        
    build:
      script:
        - docker build -t app:latest .
        
    security_scan:
      script:
        - scan_container.sh
        - verify_signatures.sh
        
    deploy:
      script:
        - deploy_to_kubernetes.sh
    """
    
    with open('files/pipeline_config.yml', 'w') as f:
        f.write(pipeline_config)
    
    # Create Kubernetes security policies
    k8s_policies = """
    apiVersion: policy/v1beta1
    kind: PodSecurityPolicy
    metadata:
      name: restricted
    spec:
      privileged: false
      allowPrivilegeEscalation: false
      requiredDropCapabilities:
        - ALL
    """
    
    with open('files/k8s_policies.yaml', 'w') as f:
        f.write(k8s_policies)

def main():
    ensure_files_directory()
    
    # Generate all challenge files
    generate_network_pentest_files()
    generate_iot_challenge_files()
    generate_cloud_challenge_files()
    generate_supply_chain_files()
    
    print("Generated ethical hacking challenge files in the files/ directory")

if __name__ == "__main__":
    main() 