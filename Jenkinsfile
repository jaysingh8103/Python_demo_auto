pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/jaysingh8103/Python_demo_auto.git'
        BRANCH = 'main'
        GITHUB_USER =''
        GITHUB_PASSWORD  = ''
        
        
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip flake8 black autopep8'
            }
        }

        stage('Linting and Static Analysis') {
            steps {
                echo 'Running flake8 for linting...'
                sh '. venv/bin/activate && flake8 --exit-zero . > flake8-report.txt || true'
            }
        }

        stage('Code Optimization') {
            steps {
                echo 'Optimizing code with autopep8 and black...'
                sh '. venv/bin/activate && autopep8 --in-place --aggressive --aggressive main.py'
                sh '. venv/bin/activate && black .'
            }
        }

        stage('Replace Unoptimized Code') {
            steps {
                echo 'Replacing unoptimized code with optimized code...'
                withCredentials([usernamePassword(credentialsId: 'github_credentials', usernameVariable: 'GITHUB_USER', passwordVariable: 'GITHUB_PASSWORD')]) {
                    sh 'git config user.name "${GITHUB_USER}"'
                    sh 'git config user.email "jaypals840@gmail.com"'
                    sh 'git add .'
                    sh 'git commit -m "Auto-optimized code via Jenkins pipeline" || true'
                    sh 'git push https://${GITHUB_USER}:${GITHUB_PASSWORD}@github.com/jaysingh8103/Python_demo_auto.git ${BRANCH}'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
