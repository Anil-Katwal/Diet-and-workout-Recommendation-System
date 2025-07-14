#!/usr/bin/env python3
"""
Simple test script to verify Flask templates are working correctly.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return render_template('index.html')

if __name__ == '__main__':
    print("Testing Flask template rendering...")
    with app.test_client() as client:
        response = client.get('/test')
        if response.status_code == 200:
            print("✅ Templates are working correctly!")
            print(f"Response length: {len(response.data)} characters")
        else:
            print(f"❌ Template test failed with status code: {response.status_code}")
            print(f"Response: {response.data.decode()}") 