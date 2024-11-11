pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  // Delete existing virtual environment if it exists, to avoid path issues
                  sh "rm -rf ${VIRTUAL_ENV}"
                  
                  // Create a new virtual environment
                  sh "python3 -m venv ${VIRTUAL_ENV}"
                  
                  // Install dependencies
                  sh "${VIRTUAL_ENV}/bin/pip install -r requirements.txt"
              }
          }
      }

      stage('Lint') {
          steps {
              script {
                  sh "${VIRTUAL_ENV}/bin/flake8 app.py"
              }
          }
      }

      stage('Test') {
          steps {
              script {
                  sh "${VIRTUAL_ENV}/bin/pytest"
              }
          }
      }

      stage('Deploy') {
          steps {
              script {
                  // Deployment logic, e.g., pushing to a remote server
                  echo "Deploying application..."
              }
          }
      }
  }

  post {
      always {
          cleanWs()
      }
  }
}
