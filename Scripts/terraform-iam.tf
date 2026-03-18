provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_user" "example_user" {
  name = "analyst1"
}

resource "aws_iam_group" "security_team" {
  name = "security-team"
}

resource "aws_iam_group_membership" "example" {
  name = "security-team-members"
  users = [aws_iam_user.example_user.name]
  group = aws_iam_group.security_team.name
}

resource "aws_iam_user_login_profile" "example" {
  user    = aws_iam_user.example_user.name
  password_reset_required = true
}
