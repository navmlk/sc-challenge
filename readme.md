# CloudFormation

## Background

This CloudFormation template orchestrates the deployment of an EC2 instance running an Amazon Linux 2 AMI behind a load balancer on AWS. The EC2 instance is configured to execute a Python script that queries the World Bank API, generating a static HTML file served by the web server.

## Implementation Details

### Part 1: Python Script
- The `endpoint.py` Python script queries the World Bank API to retrieve information about regions.
- The script orders the regions alphabetically by iso2code.
- Only the first 5 entries in the list are displayed.

### Part 2: CloudFormation Template
- The CloudFormation template (`sc-cloud-formation.yml`) defines the infrastructure components, including VPC, subnet, security group, EC2 instance, and Load Balancer.
- The EC2 instance is configured to run the `endpoint.py` Python script during initialization, generating an HTML file served by the web server.
- The template allows access to the web server only from the specified IP address.

## Limitations

1. **Customization**: The template is designed for basic demonstration purposes and may require customization for production use.
2. **AWS Account**: As I was using a sandbox account via my acloudguru.com subscription, hence I am limited to use us-east-1
2. **Security Groups**: While the template restricts access to the web server, additional security measures may be necessary depending on the use case, such as webserver & OS layer security, leveraging AWS own service (firewall, waf, shield etc)

## Future Enhancements

1. **Logging and Monitoring**: Integrate logging and monitoring solutions for improved visibility into the EC2 instance. (leveraging cloudwatch, ec2 metrics, 3rd party integation)
2. **Parameterization**: Enhance the template to accept additional parameters for increased flexibility. (CIDR Block, region, az etc)
3. **Modularize**: Enhance cloudformation template to support module (if possible)


## Instructions

### Uploading to AWS Management Console

1. Open the AWS Management Console.
2. Navigate to CloudFormation.
3. Create a new stack and upload the 'cloudformation_template.yml' file.
4. Follow the on-screen instructions to configure the stack.

### Configuring Stack Parameters

- `AllowedIPAddress`: Specify the IP address allowed to access the web server.

### Review and Create Stack

Review the stack configuration and create the stack. Once the stack is created, it will provision the necessary resources, including the EC2 instance and associated VPC components.

### Accessing the Web Server

1. Once the stack creation is complete, find the `LoadBalancerDNS` output in the CloudFormation stack details.
2. Access the web server by navigating to the provided URL.

### Cleaning Up

Remember to delete the CloudFormation stack when done to avoid ongoing charges.

## Additional Files

- `endpoint.py`: Python script for Part 1 (World Bank API query).
- `output.html`: html file to handle the output rendering.


## Feedback

If you have any feedback or questions, please feel free to provide it. Thank you!
