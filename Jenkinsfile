pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AashikAli240/easy2shop.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t easy2shop:latest .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'echo "Skipping tests on Windows agent (pytest not installed)"'
                }
            }
        }

        stage('Deploy (Docker)') {
            steps {
                script {
                    bat 'docker rm -f easy2shop || echo "No old container"'
                    bat 'docker run -d -p 5000:5000 --name easy2shop easy2shop:latest'
                }
            }
        }

        stage('Deploy (Kubernetes)') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-easy2shop', variable: 'KCFG')]) {
                    bat """
                        kubectl --kubeconfig=%KCFG% apply --validate=false -f k8s\\deployment.yaml
                    """
                }
            }
        }
    }
}
