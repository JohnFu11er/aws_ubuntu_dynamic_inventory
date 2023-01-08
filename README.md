# AWS ubuntu dynamic inventory
Example of a dynamic inventory in Python for AWS ubuntu EC2 instance configuration with Ansible. This playbook calls the `aws_inventory.py` file, which dynamically returns an inventory of the EC2 instances in your AWS envirionment. The playbook then moves through 4 tasks to install, start, enable, stop, and remove the apache package. Allows you to add or remove any number of EC2 ubuntu instances and dynamically add them to an inventory for Ansible to configure from.

- Note: This configuration assumes that you have properly configured security groups to allow SSH on port 22 between the public IP addresses of EC2 instance that you are running Ansible from, and the EC2 instances that you are configuring with Ansible.

### System requirements
- Ansible
- Python3
- Additional Python packages
  - boto3
  - requests

### Steps
1. `Launch and login` to an EC2 instance
2. Install `Ansible`
3. Install `Python`
4. Install `boto3`, and `requests` Python packages
5. `Generate an SSH keypair` on your system
6. `Upload your SSH public key` to AWS for use creating your EC2 instances
   > There are several ways to do this. The end goal is to have your private SSH key on the Ansible server, and the public key on every EC2 instance that will be configured with the Ansible script in this repo.
7. `Clone this repository` to your system
8. `Navigate to the folder` that you just cloned
9. Open the `aws_ubuntu_config.yml` file
10. Change the name of the `ansible_ssh_private_key_file:` to the name of your private key.
   - Example:
     ```
     ansible_ssh_private_key_file: ~/.ssh/id_rsa
     ```
11. Open the `aws_inventory.py` file
12. Change the `REGION` static variable to reflect the region that your EC2 instances are in.
    - Example:
      ```
      REGION = 'us-east-1'
      ```
13. Run the playbook:
    ```
    ansible-playbook aws_ubuntu_config.yml
    ```