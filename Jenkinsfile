pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
      PATH = "/usr/bin:${env.PATH}"
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  // Create a new virtual environment using the absolute path for python3
                  sh "/usr/bin/python3 -m venv ${VIRTUAL_ENV}"
                  
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
