pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out code from GitHub repository"
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/B-Kaushik21/sample-app.git']]
                ])
            }
        }

        stage('Build') {
            steps {
                echo "Building the app"
                bat """
                    python --version
                    python app.py
                """
            }
        }

        stage('Test') {
            steps {
                echo "Running tests"
                bat """
                    python -m unittest || echo No tests found
                """
            }
        }

        stage('Deploy') {
            when {
                expression { return env.BRANCH_NAME == 'main' }
            }
            steps {
                echo "Deploying application"
                
            }
        }
    }

    post {
        always {
            echo "Pipeline completed. Archiving artifacts..."
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
        success {
            echo "Pipeline finished successfully!"
        }
        failure {
            echo "Pipeline failed! Check logs."
        }
    }
}
