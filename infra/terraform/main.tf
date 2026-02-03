provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "easy2shop" {
  ami = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
}
