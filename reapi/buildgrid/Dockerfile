# Custom BuildGrid worker with mise for tool management
# Based on BuildGrid's buildbox images with mise added for dynamic tool installation
FROM registry.gitlab.com/buildgrid/buildgrid.hub.docker.com/buildbox:nightly@sha256:2a5e0a3cd87ac882cad6bdcea4bc3d0d5faf67b2f3b990340e79a40037bf00bf

USER root

# Install prerequisites
RUN apt-get update && \
    apt-get install -y curl ca-certificates gnupg unzip git && \
    rm -rf /var/lib/apt/lists/*

# Install Docker CLI (for DinD - Docker-in-Docker)
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian bookworm stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Install mise (https://mise.jdx.dev)
RUN curl https://mise.run | sh

# Configure mise
ENV MISE_TRUSTED_CONFIG_PATHS="/"
ENV MISE_YES=1

# Set up PATH to include:
# 1. mise shims (for version resolution via mise.toml)
# 2. mise binary itself
# 3. cargo/rust binaries
# 4. standard system paths
ENV PATH="/root/.local/share/mise/shims:/root/.local/bin:/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Verify mise is installed and create required directories
# Create directories that mise needs for downloads and installations
RUN mise --version && \
    mkdir -p /root/.local/share/mise/cache \
             /root/.local/share/mise/installs \
             /root/.local/share/mise/downloads \
             /root/.local/share/mise/shims \
             /root/.local/share/mise/plugins \
             /tmp/mise

# Set TMPDIR for mise to use a known-good location
ENV TMPDIR=/tmp/mise

WORKDIR /app
