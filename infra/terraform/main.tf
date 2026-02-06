# infra/terraform/main.tf
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "easy2shop" {
  ami           = "ami-xxxxxx"
  instance_type = "t3.micro"
  tags = {
    Name = "easy2shop-server"
  }
}
