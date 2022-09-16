pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "pip3 install -r requirements.txt"
                sh "python3 Final_Project_DivOps/app.py"
                
                
            }
        }
    }
}
