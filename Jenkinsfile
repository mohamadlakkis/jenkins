pipeline {
  agent any

  environment {
      VIRTUAL_ENV = 'myenv'
      PATH = "${env.WORKSPACE}/${VIRTUAL_ENV}/bin:${env.PATH}"
      PYTHONPATH = "${env.WORKSPACE}" // Adds the root directory to PYTHONPATH
  }

  stages {
      stage('Setup') {
          steps {
              script {
                  // Create a new virtual environment
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
                  // Run pytest
                  sh "${VIRTUAL_ENV}/bin/pytest"
              }
          }
      }

      stage('Deploy') {
          steps {
              script {
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
