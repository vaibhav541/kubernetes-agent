# KuberGaurd: AI-Powered Kubernetes Monitoring and Self-Healing System

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Core Features](#core-features)
4. [Agent System](#agent-system)
5. [Technology Stack](#technology-stack)
6. [Setup and Installation](#setup-and-installation)
7. [Configuration](#configuration)
8. [API Documentation](#api-documentation)
9. [User Interface Guide](#user-interface-guide)
10. [Monitoring and Observability](#monitoring-and-observability)
11. [Troubleshooting](#troubleshooting)
12. [Development Guide](#development-guide)

---

## Project Overview

KuberGaurd is an intelligent AI-powered system designed to monitor Kubernetes applications, detect performance issues, and automatically implement fixes. The system combines advanced monitoring capabilities with AI-driven decision-making to provide autonomous incident response and code optimization.

### Key Capabilities
- **Autonomous Monitoring**: Continuous monitoring of CPU and memory usage across Kubernetes pods
- **Intelligent Decision Making**: AI-powered analysis to determine appropriate remediation strategies
- **Self-Healing**: Automatic pod restarts and resource optimization
- **Code Analysis**: AI-driven code review and fix generation for persistent issues
- **GitHub Integration**: Automatic issue creation and pull request generation
- **Real-time Dashboard**: Web-based interface for monitoring and control
- **Incident Management**: Comprehensive tracking and reporting of all incidents

---

## System Architecture

### High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web UI        │    │   Chat Interface│    │   Dashboard     │
│   (Port 8080)   │    │                 │    │   Monitoring    │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴───────────┐
                    │      API Gateway        │
                    │      (Port 8000)        │
                    └─────────────┬───────────┘
                                  │
                    ┌─────────────┴───────────┐
                    │      AI Agent           │
                    │   (LangGraph-based)     │
                    │      (Port 8002)        │
                    └─────────────┬───────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
┌─────────┴───────┐    ┌─────────┴───────┐    ┌─────────┴───────┐
│  MCP Servers    │    │  Monitoring     │    │  Test App       │
│                 │    │  Stack          │    │                 │
│ • Kubernetes    │    │ • Prometheus    │    │ • Simulation    │
│ • Prometheus    │    │ • Grafana       │    │ • Metrics       │
│ • Grafana       │    │                 │    │                 │
│ • GitHub        │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Overview

#### 1. **AI Agent Core** (Port 8002)
- **Technology**: LangGraph + Anthropic Claude
- **Purpose**: Central decision-making engine
- **Responsibilities**: Workflow orchestration, AI-powered analysis, action routing

#### 2. **API Gateway** (Port 8000)
- **Technology**: FastAPI
- **Purpose**: Request routing and API management
- **Responsibilities**: HTTP endpoints, WebSocket connections, request validation

#### 3. **Web UI** (Port 8080)
- **Technology**: HTML/CSS/JavaScript
- **Purpose**: User interface and dashboard
- **Responsibilities**: Real-time monitoring, incident management, simulation controls

#### 4. **Test Application** (Port 8001)
- **Technology**: FastAPI + Prometheus metrics
- **Purpose**: Simulated workload for testing
- **Responsibilities**: CPU/memory spike simulation, metrics generation

#### 5. **MCP Servers** (Ports 5001-5004)
- **Technology**: FastAPI-based microservices
- **Purpose**: External system integration
- **Components**:
  - Kubernetes MCP (5001): Pod management and monitoring
  - Prometheus MCP (5002): Metrics querying
  - Grafana MCP (5003): Dashboard management
  - GitHub MCP (5004): Issue and PR management

#### 6. **Monitoring Stack**
- **Prometheus** (Port 9090): Metrics collection and storage
- **Grafana** (Port 3000): Visualization and dashboards

---

## Core Features

### 1. **Intelligent Monitoring**

#### Metrics Collection
- **CPU Usage**: Real-time CPU percentage monitoring
- **Memory Usage**: Memory consumption in bytes
- **Spike Detection**: Automatic detection of resource spikes
- **Pod Health**: Kubernetes pod status and health checks

#### Thresholds
- **CPU Threshold**: 10% (configurable, lowered for testing)
- **Memory Threshold**: 600MB (configurable)
- **Severity Calculation**: Dynamic severity based on threshold multipliers
  - Low: 1.0x - 1.2x threshold
  - Medium: 1.2x - 1.5x threshold
  - High: >1.5x threshold

### 2. **Self-Healing Capabilities**

#### Automatic Pod Restart
- **Trigger**: Resource usage exceeds thresholds
- **Limit**: Maximum 10 restarts per day per pod
- **Tracking**: Persistent restart count with daily reset
- **Escalation**: Code analysis after 4 restarts

#### Intelligent Escalation
```
Issue Detected → Pod Restart (1-4 times) → Code Analysis → PR Creation
```

### 3. **AI-Powered Code Analysis**

#### Analysis Process
1. **Log Retrieval**: Extract recent pod logs (1000 lines)
2. **Code Inspection**: Retrieve application source code
3. **AI Analysis**: Claude-based code review and issue identification
4. **Fix Generation**: Complete code fixes with explanations
5. **PR Creation**: Automatic pull request with proposed changes

#### Generated Artifacts
- **GitHub Issues**: Detailed incident reports
- **Pull Requests**: Code fixes with comprehensive descriptions
- **Grafana Annotations**: Timeline markers for incidents

### 4. **Comprehensive Incident Management**

#### Incident Tracking
- **Unique IDs**: UUID-based incident identification
- **Metadata**: Timestamp, severity, pod information, metrics
- **Actions**: Record of all remediation actions taken
- **GitHub Integration**: Linked issues and pull requests

#### Incident Types
- **CPU**: High CPU usage incidents
- **Memory**: Memory consumption issues
- **Mixed**: Combined resource issues

---

## Agent System

KuberGaurd employs a multi-agent architecture where specialized AI agents handle different aspects of the monitoring and remediation process.

### Agent Workflow

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│  Seer   │───▶│ Oracle  │───▶│ Medic/  │───▶│ Herald  │
│ Monitor │    │ Decide  │    │ Smith   │    │ Format  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │
     ▼              ▼              ▼              ▼
  Metrics      Decision       Action         Response
Collection    Making        Execution      Formatting
```

### 1. **Seer Agent** - The Observer
**Role**: Metrics monitoring and analysis

**Responsibilities**:
- Query Prometheus for CPU and memory metrics
- Retrieve Kubernetes pod information
- Process and normalize metric data
- Detect threshold violations
- Calculate issue severity

**Key Functions**:
```python
def monitor_metrics(state: AgentState) -> AgentState:
    # Query Prometheus for metrics
    # Get Kubernetes pod status
    # Process and analyze data
    # Return structured metrics
```

**Logging**: Detailed monitoring logs with metric values and analysis results

### 2. **Oracle Agent** - The Decision Maker
**Role**: Intelligent decision-making and workflow routing

**Responsibilities**:
- Analyze detected issues
- Check restart history
- Determine appropriate action (restart vs. code analysis)
- Route workflow to appropriate agent

**Decision Logic**:
```python
if restart_count >= ANALYSIS_THRESHOLD:
    return "analyze_code"
elif restart_count < MAX_RESTARTS_PER_DAY:
    return "remediate"
else:
    return "remediate"  # Final restart before escalation
```

### 3. **Medic Agent** - The Healer
**Role**: Issue remediation and immediate response

**Responsibilities**:
- Execute pod restarts
- Create GitHub issues for incidents
- Update restart counters
- Generate Grafana annotations
- Track incident records

**Remediation Process**:
1. Identify most severe issue
2. Restart affected pod
3. Increment restart counter
4. Create detailed GitHub issue
5. Log incident in system
6. Update monitoring dashboard

### 4. **Smith Agent** - The Code Analyst
**Role**: Deep code analysis and fix generation

**Responsibilities**:
- Retrieve pod logs and application code
- Perform AI-powered code analysis
- Generate complete code fixes
- Create GitHub branches and pull requests
- Provide detailed analysis reports

**Analysis Workflow**:
1. **Data Collection**: Gather logs and source code
2. **AI Analysis**: Use Claude to identify issues
3. **Fix Generation**: Create complete code solutions
4. **GitHub Integration**: Create branches, files, and PRs
5. **Documentation**: Generate comprehensive analysis reports

### 5. **Forge Agent** - The Record Keeper
**Role**: Incident management and GitHub integration

**Responsibilities**:
- Maintain incident database
- Create and manage GitHub issues
- Track restart counts and history
- Generate incident reports
- Manage incident lifecycle

**Data Management**:
- In-memory incident storage with persistence
- Daily restart count tracking
- Incident filtering and querying
- GitHub issue/PR correlation

### 6. **Vision Agent** - The Visualizer
**Role**: Dashboard updates and visual feedback

**Responsibilities**:
- Create Grafana annotations
- Update dashboard panels
- Provide visual incident markers
- Maintain monitoring visualizations

### 7. **Herald Agent** - The Communicator
**Role**: Response formatting and communication

**Responsibilities**:
- Format final responses for API
- Structure data for UI consumption
- Handle error messaging
- Coordinate agent communications

---

## Technology Stack

### Core Technologies

#### Backend
- **Python 3.9+**: Primary programming language
- **FastAPI**: Web framework for APIs and MCP servers
- **LangGraph**: AI workflow orchestration
- **Anthropic Claude**: Large language model for analysis
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server

#### AI/ML
- **LangChain**: LLM integration framework
- **Anthropic API**: Claude 3 Sonnet model
- **OpenAI API**: Alternative LLM support (configurable)
- **Azure OpenAI**: Enterprise LLM option

#### Monitoring
- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboards
- **prometheus_client**: Python metrics library

#### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Kubernetes**: Container orchestration (target platform)

#### Frontend
- **HTML/CSS/JavaScript**: Web interface
- **Socket.IO**: Real-time communication
- **Font Awesome**: Icons and UI elements
- **Inter & Fira Code**: Typography

#### External Integrations
- **GitHub API**: Issue and PR management
- **PyGithub**: Python GitHub client
- **Kubernetes API**: Pod management
- **Requests**: HTTP client library

### Development Tools
- **python-dotenv**: Environment variable management
- **psutil**: System resource monitoring
- **uuid**: Unique identifier generation
- **logging**: Comprehensive logging system

---

## Setup and Installation

### Prerequisites
- **Docker & Docker Compose**: Latest versions
- **Python 3.9+**: For local development
- **Git**: Version control
- **GitHub Account**: For issue/PR integration
- **API Keys**: Anthropic Claude API key

### Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/kubergaurd.git
cd kubergaurd
```

2. **Environment Setup**
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your API keys
nano .env
```

3. **Required Environment Variables**
```bash
# AI/LLM Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# GitHub Integration
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_OWNER=your_github_username_or_org
GITHUB_REPO=kubergaurd

# Agent Configuration (optional, has defaults)
MAX_RESTARTS_PER_DAY=10
ANALYSIS_THRESHOLD=4
CPU_THRESHOLD=10
MEMORY_THRESHOLD=600000000
```

4. **Start the System**
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

5. **Access the Interface**
- **Web UI**: http://localhost:8080
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090
- **API**: http://localhost:8000

### Manual Installation

1. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

2. **Install Agent Dependencies**
```bash
cd src/agent
pip install -r requirements.txt
```

3. **Start Services Individually**
```bash
# Terminal 1: Start Prometheus
docker run -p 9090:9090 -v ./src/monitoring/prometheus:/etc/prometheus prom/prometheus

# Terminal 2: Start Grafana
docker run -p 3000:3000 -e GF_SECURITY_ADMIN_PASSWORD=admin grafana/grafana

# Terminal 3: Start Test App
cd src/api
uvicorn main:app --host 0.0.0.0 --port 8001

# Terminal 4: Start Agent
cd src/agent
uvicorn api:app --host 0.0.0.0 --port 8002

# Terminal 5: Start UI
cd src/ui
node server.js
```

---

## Configuration

### Environment Variables

#### AI/LLM Configuration
```bash
# Primary AI provider (currently used)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Alternative providers (optional)
OPENAI_API_KEY=your_openai_api_key_here
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

#### GitHub Integration
```bash
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_OWNER=your_github_username_or_org
GITHUB_REPO=kubergaurd
```

**GitHub Token Permissions Required**:
- `repo`: Full repository access
- `issues`: Read/write issues
- `pull_requests`: Read/write pull requests

#### Agent Behavior
```bash
# Maximum pod restarts per day before escalation
MAX_RESTARTS_PER_DAY=10

# Number of restarts that triggers code analysis
ANALYSIS_THRESHOLD=4

# Resource thresholds
CPU_THRESHOLD=10          # CPU percentage
MEMORY_THRESHOLD=600000000 # Memory in bytes (600MB)
```

#### Service URLs (Docker Network)
```bash
KUBERNETES_MCP_URL=http://kubernetes-mcp:5001
PROMETHEUS_MCP_URL=http://prometheus-mcp:5002
GRAFANA_MCP_URL=http://grafana-mcp:5003
GITHUB_MCP_URL=http://github-mcp:5004
PROMETHEUS_URL=http://prometheus:9090
GRAFANA_URL=http://grafana:3000
```

#### Feature Flags
```bash
ENABLE_AUTO_RESTART=true
ENABLE_GITHUB_ISSUES=true
ENABLE_GITHUB_PRS=true
ENABLE_GRAFANA_ANNOTATIONS=true
ENABLE_CODE_ANALYSIS=true
```

### Customization Options

#### Threshold Adjustment
Modify thresholds based on your application requirements:
```bash
# For production workloads
CPU_THRESHOLD=80
MEMORY_THRESHOLD=2147483648  # 2GB

# For development/testing
CPU_THRESHOLD=10
MEMORY_THRESHOLD=600000000   # 600MB
```

#### Restart Policy
```bash
# Conservative approach
MAX_RESTARTS_PER_DAY=5
ANALYSIS_THRESHOLD=2

# Aggressive approach
MAX_RESTARTS_PER_DAY=20
ANALYSIS_THRESHOLD=10
```

---

## API Documentation

### Core Endpoints

#### Agent API (Port 8002)

##### POST `/agent/run`
Trigger agent workflow execution
```json
{
  "input": {}
}
```

**Response**:
```json
{
  "status": "success",
  "action": "remediate",
  "pod_name": "test-app-xyz",
  "namespace": "default",
  "issue_type": "cpu",
  "restart_count": 3,
  "github_issue_number": 42,
  "github_issue_url": "https://github.com/user/repo/issues/42",
  "incident_id": "uuid-string"
}
```

##### GET `/incidents`
Retrieve incidents with filtering
```
GET /incidents?type=cpu&resolved=false&limit=10
```

**Response**:
```json
[
  {
    "id": "incident-uuid",
    "type": "cpu",
    "pod_name": "test-app",
    "namespace": "default",
    "timestamp": 1640995200,
    "severity": "high",
    "metrics": {
      "value": 85.5,
      "threshold": 80
    },
    "action_taken": "restart_pod",
    "github_issue": {
      "number": 42,
      "html_url": "https://github.com/user/repo/issues/42"
    }
  }
]
```

##### GET `/restart-counts`
Get pod restart statistics
```json
{
  "2024-01-01": {
    "test-app": 3,
    "api-server": 1
  },
  "2024-01-02": {
    "test-app": 2
  }
}
```

#### Test Application API (Port 8001)

##### GET `/status`
Get current application status
```json
{
  "cpu_usage": 45.2,
  "memory_usage": 524288000,
  "cpu_spike_active": false,
  "memory_spike_active": true
}
```

##### POST `/simulate/cpu`
Trigger CPU spike simulation
```json
{
  "status": "started",
  "message": "CPU spike simulation started. Will run for 60 seconds."
}
```

##### POST `/simulate/memory`
Trigger memory spike simulation
```json
{
  "status": "started",
  "message": "Memory spike simulation started. Will run for 120 seconds."
}
```

##### POST `/simulate/stop`
Stop all simulations (simulates pod restart)
```json
{
  "status": "stopped",
  "message": "All simulations stopped (simulating pod restart)"
}
```

#### MCP Server APIs

##### Kubernetes MCP (Port 5001)
- `POST /mcp/tools/list_pods`: List Kubernetes pods
- `POST /mcp/tools/restart_pod`: Restart a specific pod
- `POST /mcp/tools/get_logs`: Retrieve pod logs
- `POST /mcp/tools/get_app_code`: Get application source code

##### Prometheus MCP (Port 5002)
- `POST /mcp/tools/query`: Execute PromQL queries
- `POST /mcp/tools/query_range`: Execute range queries
- `POST /mcp/tools/alerts`: Get active alerts
- `POST /mcp/tools/targets`: Get scrape targets

##### Grafana MCP (Port 5003)
- `POST /mcp/tools/create_annotation`: Create dashboard annotations
- `POST /mcp/tools/update_panel`: Update dashboard panels
- `POST /mcp/tools/get_dashboards`: List available dashboards

##### GitHub MCP (Port 5004)
- `POST /mcp/tools/create_issue`: Create GitHub issues
- `POST /mcp/tools/create_pull_request`: Create pull requests
- `POST /mcp/tools/create_branch`: Create new branches
- `POST /mcp/tools/create_file`: Create files in repository

### WebSocket Communication

#### Real-time Updates
The system provides real-time updates via WebSocket connections:

```javascript
const socket = io('http://localhost:8000');

socket.on('agent_log', (data) => {
  console.log('Agent Log:', data);
});

socket.on('incident_created', (incident) => {
  console.log('New Incident:', incident);
});

socket.on('pod_restarted', (data) => {
  console.log('Pod Restarted:', data);
});
```

---

## User Interface Guide

### Dashboard Overview

The web interface provides comprehensive monitoring and control capabilities through multiple views:

#### 1. **Dashboard View**
- **Services Health**: Real-time status of all system components
- **Recent Incidents**: Latest incidents with severity indicators
- **Restart Counts**: Pod restart statistics performed by the agent
- **Quick Actions**: Common operations (restart pod, view incidents)
- **Agent Logs**: Real-time agent activity logs

#### 2. **Incidents View**
- **Incident List**: Comprehensive incident history
- **Filtering**: Filter by type (CPU/Memory) and status (Active/Resolved)
- **Details**: Detailed incident information with GitHub links
- **Refresh**: Manual refresh capability

#### 3. **Simulate View**
- **Trading Paths**: Simulate CPU-intensive operations
- **Trade Fetching**: Simulate memory-intensive operations
- **Pod Restart**: Manual pod restart functionality
- **Status Display**: Current simulation status

#### 4. **Settings View**
- **Agent Configuration**: Modify agent behavior parameters
- **Thresholds**: Adjust CPU and memory thresholds
- **Intervals**: Configure monitoring intervals
- **Save Settings**: Persist configuration changes

### Chat Interface

#### GOA Assistant
The integrated chat assistant provides:
- **Help Commands**: Quick access to common operations
- **Incident Queries**: Natural language incident investigation
- **Pod Management**: Restart and status commands
- **Real-time Feedback**: Live updates on agent activities

#### Available Commands
- `help`: Show available commands
- `restart pod`: Trigger pod restart
- `show incidents`: Display recent incidents
- `status`: Get system status
- `simulate cpu`: Start CPU spike simulation
- `simulate memory`: Start memory spike simulation

### Navigation

#### Sidebar Menu
- **Dashboard**: Main monitoring view
- **Incidents**: Incident management
- **Simulate**: Testing and simulation tools
- **Settings**: Configuration options

#### Status Indicators
- **Green**: Healthy/Normal operation
- **Yellow**: Warning/Attention needed
- **Red**: Critical/Error state
- **Gray**: Unknown/Disconnected

---

## Monitoring and Observability

### Metrics Collection

#### Application Metrics
The test application exposes Prometheus metrics on port 8001:

```python
# CPU usage percentage
app_cpu_usage_percent

# Memory usage in bytes
app_memory_usage_bytes

# CPU spike counter
app_cpu_spike_total

# Memory spike counter
app_memory_spike_total

# Request latency histogram
app_request_latency_seconds
```

#### Agent Metrics
The AI agent system provides comprehensive logging:

```python
# Agent-specific loggers
seer_logger    # Monitoring and metrics analysis
oracle_logger  # Decision making
medic_logger   # Remediation actions
smith_logger   # Code analysis
forge_logger   # Incident management
vision_logger  # Dashboard updates
herald_logger  # Communication
```

### Grafana Dashboards

#### Default Dashboard Configuration
Located in `src/monitoring/grafana/dashboards/`:

- **CPU Usage Panel**: Real-time CPU percentage
- **Memory Usage Panel**: Memory consumption in bytes
- **Spike Counters**: Total spikes over time
- **Pod Status**: Kubernetes pod health
- **Incident Annotations**: Timeline markers for incidents

#### Custom Queries
```promql
# CPU usage over time
app_cpu_usage_percent

# Memory usage in MB
app_memory_usage_bytes / 1024 / 1024

# Spike rate per hour
rate(app_cpu_spike_total[1h]) * 3600
```

### Logging Strategy

#### Log Levels
- **DEBUG**: Detailed execution information
- **INFO**: General operational messages
- **WARNING**: Potential issues or important events
- **ERROR**: Error conditions requiring attention

#### Log Format
```
[TIMESTAMP] [LEVEL] [AGENT] Message with context
```

Example:
```
[2024-01-01 12:00:00] [INFO] [Seer] Seer is starting to monitor metrics
[2024-01-01 12:00:01] [WARNING] [Oracle] Oracle determines restart count 5 exceeds threshold
[2024-01-01 12:00:02] [ERROR] [Medic] Error restarting pod: Connection timeout
```

### Alerting

#### Prometheus Alerting Rules
```yaml
groups:
  - name: kubergaurd
    rules:
      - alert: HighCPUUsage
        expr: app_cpu_usage_percent > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage detected"
          
      - alert: HighMemoryUsage
        expr: app_memory_usage_bytes > 1073741824  # 1GB
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage detected"
```

---

## Troubleshooting

### Common Issues

#### 1. **Agent Not Starting**
**Symptoms**: Agent container fails to start or crashes immediately

**Possible Causes**:
- Missing or invalid API keys
- Network connectivity issues
- Port conflicts

**Solutions**:
```bash
# Check environment variables
docker-compose exec agent env | grep -E "(ANTHROPIC|GITHUB)"

# Check logs
docker-compose logs agent

# Verify API key
curl -H "Authorization: Bearer $ANTHROPIC_API_KEY" https://api.anthropic.com/v1/messages
```

#### 2. **GitHub Integration Failing**
**Symptoms**: Issues not created, PRs failing

**Possible Causes**:
- Invalid GitHub token
- Insufficient permissions
- Repository not accessible

**Solutions**:
```bash
# Test GitHub token
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user

# Check repository access
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO

# Verify token permissions in GitHub settings
```

#### 3. **Metrics Not Appearing**
**Symptoms**: Prometheus shows no data, Grafana dashboards empty

**Possible Causes**:
- Test application not running
- Prometheus configuration issues
- Network connectivity problems

**Solutions**:
```bash
# Check test app metrics endpoint
curl http://localhost:8001/metrics

# Verify Prometheus targets
curl http://localhost:9090/api/v1/targets

# Check Prometheus configuration
docker-compose exec prometheus cat /etc/prometheus/prometheus.yml
```

#### 4. **Pod Restart Failures**
**Symptoms**: Agent reports restart failures, pods not restarting

**Possible Causes**:
- Kubernetes API access issues
- Insufficient permissions
- Pod not found

**Solutions**:
```bash
# Check Kubernetes MCP server
curl http://localhost:5001/health

# Test pod listing
curl -X POST http://localhost:5001/mcp/tools/list_pods \
  -H "Content-Type: application/json" \
  -d '{"namespace": "default"}'
```

### Debug Mode

#### Enable Debug Logging
```bash
# Set in .env file
DEBUG=true
LOG_LEVEL=DEBUG

# Restart services
docker-compose restart
```

#### Agent Workflow Debugging
```python
# Add to agent.py for detailed state inspection
import json
print(f"Agent State: {json.dumps(state, indent=2)}")
```

### Performance Issues

#### High Memory Usage
```bash
# Monitor container memory
docker stats

# Check for memory leaks in test app
curl http://localhost:8001/status
```

#### Slow Response Times
```bash
# Check agent processing time
docker-compose logs agent | grep "workflow completed"

# Monitor API response times
curl -w "@curl-format.txt" http://localhost:8000/health
```

### Network Issues

#### Port Conflicts
```bash
# Check port usage
lsof -i :8080
lsof -i :3000
lsof -i :9090

# Modify ports in docker-compose.yml if needed
```

#### DNS Resolution
```bash
# Test internal DNS
docker-compose exec agent nslookup prometheus
docker-compose exec agent nslookup grafana
```

---

## Development Guide

### Project Structure

```
kubergaurd/
├── .env                    # Environment configuration
├── .env.example           # Environment template
├── docker-compose.yml     # Container orchestration
├── requirements.txt       # Python dependencies
├── README.md             # Basic project information
├── DOCUMENTATION.md      # This comprehensive guide
└── src/
    ├── agent/            # AI Agent implementation
    │   ├── agent.py      # Main agent workflow
    │   ├── api.py        # Agent API endpoints
    │   ├── mcp_client.py # MCP client management
    │   ├── incident_store.py # Incident data management
    │   ├── requirements.txt
    │   ├── Dockerfile
    │   └── sub_agents/   # Specialized agent modules
    │       ├── seer.py   # Monitoring agent
    │       ├── oracle.py # Decision agent
    │       ├── medic.py  # Remediation agent
    │       ├── smith.py  # Code analysis agent
    │       ├── forge.py  # Incident management agent
    │       ├── vision.py # Dashboard agent
    │       ├── herald.py # Communication agent
    │       └── logger.py # Logging configuration
    ├── api/              # Test application
    │   ├── main.py       # FastAPI test app
    │   ├── requirements.txt
    │   └── Dockerfile
    ├── mcp/              # MCP server implementations
    │   ├── kubernetes/   # Kubernetes integration
    │   ├── prometheus/   # Prometheus integration
    │   ├── grafana/      # Grafana integration
    │   └── github/       # GitHub integration
    ├── monitoring/       # Monitoring configuration
    │   ├── prometheus/   # Prometheus config
    │   └── grafana/      # Grafana dashboards
    └── ui/               # Web interface
        ├── server.js     # Node.js server
        ├── package.json
        ├── Dockerfile
        └── public/       # Static web assets
            ├── index.html
            ├── app.js
            ├── styles.css
            └── imgs/
```

### Adding New Agents

#### 1. Create Agent Module
```python
# src/agent/sub_agents/new_agent.py
from .logger import new_agent_logger

def new_agent_function(state: AgentState) -> AgentState:
    """New Agent: Description of functionality"""
    new_agent_logger.info("New agent starting operation")
    
    # Agent logic here
    
    return {
        **state,
        "new_data": processed_data
    }
```

#### 2. Update Main Workflow
```python
# src/agent/agent.py
from sub_agents.new_agent import new_agent_function

# Add to workflow
workflow.add_node("new_agent", new_agent_function)
workflow.add_edge("previous_node", "new_agent")
workflow.add_edge("new_agent", "next_node")
```

#### 3. Update Logger Configuration
```python
# src/agent/sub_agents/logger.py
new_agent_logger = logging.getLogger("new_agent")
```

### Adding New MCP Servers

#### 1. Create MCP Server Directory
```bash
mkdir src/mcp/new_service
cd src/mcp/new_service
```

#### 2. Implement MCP Server
```python
# src/mcp/new_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="New Service MCP Server")

class NewServiceInput(BaseModel):
    parameter: str

class NewServiceOutput(BaseModel):
    result: str

@app.post("/mcp/tools/new_action", response_model=NewServiceOutput)
async def new_action(input_data: NewServiceInput):
    # Implementation here
    return NewServiceOutput(result="success")

@app.get("/mcp/schema")
async def get_schema():
    return {
        "name": "new-service-mcp",
        "version": "1.0.0",
        "tools": [
            {
                "name": "new_action",
                "description": "Perform new action",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "parameter": {"type": "string"}
                    },
                    "required": ["parameter"]
                }
            }
        ]
    }
```

#### 3. Add to Docker Compose
```yaml
# docker-compose.yml
new-service-mcp:
  build:
    context: ./src/mcp/new_service
    dockerfile: Dockerfile
  ports:
    - "5005:5005"
  networks:
    - app-network
```

### Testing

#### Unit Tests
```python
# tests/test_agents.py
import pytest
from src.agent.sub_agents.seer import monitor_metrics

def test_monitor_metrics():
    state = {"input": {}}
    result = monitor_metrics(state)
    assert "metrics" in result
    assert result["error"] is None
```

#### Integration Tests
```python
# tests/test_integration.py
import requests

def test_agent_workflow():
    response = requests.post("http://localhost:8002/agent/run")
    assert response.status_code == 200
    assert "status" in response.json()
```

#### Load Testing
```bash
# Install artillery
npm install -g artillery

# Create load test config
cat > load-test.yml << EOF
config:
  target: 'http://localhost:8000'
  phases:
    - duration: 60
      arrivalRate: 10
scenarios:
  - name: "Agent workflow"
    requests:
      - post:
          url: "/agent/run"
          json:
            input: {}
EOF

# Run load test
artillery run load-test.yml
```

### Deployment

#### Production Environment Variables
```bash
# Production .env
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO

# Use production-grade LLM endpoints
ANTHROPIC_API_KEY=prod_key_here

# Production GitHub repository
GITHUB_REPO=kubergaurd-prod

# Higher thresholds for production
CPU_THRESHOLD=80
MEMORY_THRESHOLD=2147483648

# Conservative restart policy
MAX_RESTARTS_PER_DAY=5
ANALYSIS_THRESHOLD=2
```

#### Kubernetes Deployment
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubergaurd-agent
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kubergaurd-agent
  template:
    metadata:
      labels:
        app: kubergaurd-agent
    spec:
      containers:
      - name: agent
        image: kubergaurd/agent:latest
        ports:
        - containerPort: 8000
        env:
        - name: ANTHROPIC_API_KEY
          valueFrom:
            secretKeyRef:
              name: kubergaurd-secrets
              key: anthropic-api-key
        - name: GITHUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: kubergaurd-secrets
              key: github-token
```

#### Docker Production Build
```dockerfile
# Dockerfile.prod
FROM python:3.9-slim

WORKDIR /app

# Install production dependencies only
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Create non-root user
RUN useradd -m -u 1000 kubergaurd
USER kubergaurd

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["uvicorn", "src.agent.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Security Considerations

#### API Security
- **Authentication**: Implement JWT-based authentication
- **Rate Limiting**: Prevent API abuse
- **Input Validation**: Validate all inputs
- **HTTPS**: Use TLS in production

#### Secrets Management
- **Environment Variables**: Never commit secrets to version control
- **Kubernetes Secrets**: Use for production deployments
- **Vault Integration**: For enterprise secret management

#### Network Security
- **Firewall Rules**: Restrict network access
- **VPN**: Use VPN for remote access
- **Network Policies**: Implement Kubernetes network policies

### Performance Optimization

#### Agent Performance
```python
# Async processing for better performance
import asyncio

async def async_monitor_metrics(state: AgentState) -> AgentState:
    tasks = [
        query_prometheus_async(),
        get_kubernetes_pods_async(),
        check_api_status_async()
    ]
    results = await asyncio.gather(*tasks)
    return process_results(results)
```

#### Database Optimization
```python
# Use connection pooling
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

#### Caching
```python
# Redis caching for frequently accessed data
import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)

def get_cached_metrics(pod_name: str):
    cached = redis_client.get(f"metrics:{pod_name}")
    if cached:
        return json.loads(cached)
    return None
```

---

## Contributing

### Development Workflow

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/new-feature`
3. **Make Changes**: Implement your feature
4. **Add Tests**: Ensure good test coverage
5. **Run Tests**: `pytest tests/`
6. **Update Documentation**: Update relevant documentation
7. **Submit Pull Request**: Create PR with detailed description

### Code Style

#### Python Code Style
- **PEP 8**: Follow Python style guidelines
- **Type Hints**: Use type annotations
- **Docstrings**: Document all functions and classes
- **Black**: Use Black for code formatting

```bash
# Install development dependencies
pip install black pytest flake8 mypy

# Format code
black src/

# Run linting
flake8 src/

# Type checking
mypy src/
```

#### Commit Messages
```
feat: add new monitoring agent
fix: resolve memory leak in metrics collection
docs: update API documentation
test: add integration tests for GitHub MCP
refactor: improve agent workflow performance
```

### Issue Reporting

When reporting issues, please include:
- **Environment**: OS, Python version, Docker version
- **Configuration**: Relevant environment variables (redacted)
- **Steps to Reproduce**: Clear reproduction steps
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Logs**: Relevant log output
- **Screenshots**: If applicable

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Anthropic**: For providing the Claude AI model
- **LangChain**: For the LLM integration framework
- **Prometheus**: For metrics collection
- **Grafana**: For visualization
- **FastAPI**: For the web framework
- **Docker**: For containerization

---

## Support

For support and questions:
- **GitHub Issues**: Report bugs and request features
- **Documentation**: Refer to this comprehensive guide
- **Community**: Join our community discussions

---

*This documentation is maintained by the KuberGaurd development team. Last updated: January 2024*
