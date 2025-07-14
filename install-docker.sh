#!/bin/bash

echo "Docker Installation Helper for macOS"
echo "===================================="

# Check if Docker is already installed
if command -v docker &> /dev/null; then
    echo "Docker is already installed!"
    docker --version
    exit 0
fi

echo "Docker is not installed. Here are your options:"
echo ""
echo "1. Install Docker Desktop (Recommended for macOS):"
echo "   - Visit: https://www.docker.com/products/docker-desktop"
echo "   - Download and install Docker Desktop for Mac"
echo "   - Follow the installation wizard"
echo ""
echo "2. Install via Homebrew:"
echo "   brew install --cask docker"
echo ""
echo "3. Manual installation:"
echo "   - Download from: https://docs.docker.com/desktop/install/mac-install/"
echo ""
echo "After installation:"
echo "1. Start Docker Desktop"
echo "2. Wait for Docker to be ready (green icon in menu bar)"
echo "3. Run: docker --version"
echo "4. Then you can use: docker-compose up --build"
echo ""
echo "For more information, see: https://docs.docker.com/desktop/install/mac-install/" 