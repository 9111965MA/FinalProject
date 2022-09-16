pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "python3 Final_Project_DivOps/app.py"
                sh "pip3 install -r requirement.txt"
            }
        }
