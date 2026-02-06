pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat'pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                bat'pytest || echo "No tests yet"'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat'docker build -t easy2shop:latest .'
            }
        }

        stage('Pubatto Registry') {
            steps {
                bat'docker tag easy2shop:latest <registry>/easy2shop:latest'
                bat'docker pubat<registry>/easy2shop:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat'kubectl apply -f k8s/deployment.yaml'
                bat'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}
