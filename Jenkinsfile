pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'
        VENV_DIR = 'venv'
        PROJECT_NAME = 'django'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/twist1990/django-'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh "python${PYTHON_VERSION} -m venv ${VENV_DIR}"
                sh ". ${VENV_DIR}/bin/activate && pip install --upgrade pip"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh ". ${VENV_DIR}/bin/activate && pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh ". ${VENV_DIR}/bin/activate && python manage.py test"
            }
        }

        stage('Build Docker Image (Optional)') {
            steps {
                script {
                    docker.build("${PROJECT_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Example: Deploy to a remote server using SSH
                    sshagent(['your-ssh-credentials-id']) {
                        sh "scp -r . user@your-server:/path/to/deploy"
                        sh "ssh user@your-server 'cd /path/to/deploy && ./deploy.sh'"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
