# CARDESC

## Overview

CARDESC is a Python-based application that simulates a bank card payment page interface. The application includes a local PHP server for hosting payment pages, logging functionality, Telegram bot integration for notifications, and an AI assistant powered by OpenAI for user queries.

**Note:** This repository contains code for educational/research purposes related to understanding payment security mechanisms.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Components

1. **Main Application (bank.py)**
   - Entry point for the application
   - Provides a menu-driven interface with options for viewing history, starting payment pages, configuring settings, and accessing help
   - Uses multiprocessing to run the PHP server and monitoring processes concurrently

2. **PHP Payment Server**
   - Serves static payment page files from the `dist/` directory
   - Runs on a configurable local port using PHP's built-in server
   - Logs payment card details to `dist/details/log.log`

3. **Server Monitor (Delpha class)**
   - Continuously reads and displays logged data in a formatted table using PrettyTable
   - Refreshes display every second to show new entries

4. **AI Assistant (assistant.py)**
   - Integrates with OpenAI API (GPT-5) via Replit's AI Integrations service
   - Provides a conversational interface for banking-related queries
   - Uses environment variables for API authentication

### Design Patterns

- **Callable Classes**: `Alpha` and `Delpha` classes use `__call__` method to make instances callable, encapsulating server and monitor logic
- **Multiprocessing**: Separates PHP server execution from the monitoring display
- **Configuration-Driven**: Uses JSON metadata file for version info and external URLs

### Data Flow

1. User starts the application and selects payment page option
2. PHP server starts serving payment page on specified port
3. User interactions on payment page are logged to `log.log`
4. Monitor process reads log file and displays data in real-time table format
5. Optional: Data can be sent to Telegram bot via API

## External Dependencies

### Python Packages
- **prettytable**: Formats logged data into readable ASCII tables
- **requests**: Handles HTTP requests for update checking and Telegram API
- **openai**: Provides OpenAI API client for AI assistant functionality

### Runtime Requirements
- **PHP**: Required for running the local payment page server (`php -S` command)
- **Python 3**: Main application runtime

### External Services
- **Telegram Bot API**: Sends logged payment data to configured Telegram chat
- **OpenAI API**: Powers the AI assistant (accessed via Replit's AI Integrations)
  - Uses `AI_INTEGRATIONS_OPENAI_API_KEY` environment variable
  - Uses `AI_INTEGRATIONS_OPENAI_BASE_URL` environment variable
- **GitHub Raw Content**: Fetches version metadata for update checking from `raw.githubusercontent.com`

### Configuration Files
- **info/metadata.json**: Stores application metadata including version, author info, and update URL
- **dist/details/log.log**: Runtime log file for payment data (created during execution)