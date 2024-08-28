# Synthetic Monitoring Project

## Overview
This repository contains code for a synthetic monitoring project designed to continuously simulate user interactions with a system to monitor and verify network and application health. Synthetic monitoring helps in detecting outages and performance issues before they affect actual users.

## Why Synthetic Monitoring?
1. **Proactive Problem Detection:** Synthetic monitoring can identify problems before they impact users by continuously checking critical endpoints and services.
2. **Performance Benchmarking:** It helps in tracking the performance of your services over time and understanding the impact of changes.
3. **Availability Metrics:** Provides data on system availability and responsiveness, which are key to service level agreements (SLAs) and customer satisfaction.

## Project Structure
The project is divided into four parts, each responsible for a different aspect of synthetic monitoring.

### Part-1
1) **Function:** Parses a YAML file and prints the data to the console.
2) **Error Handling:** Raises an exception if any occurs during the parsing process.

### Part-2
1) **Library Used:** [`pingparsing`](https://pypi.org/project/pingparsing/)
2) **Function:** Pings a server provided by the user and outputs the ping metrics to the console.

### Part-3
1) **Integration:** Combines Part-1 and Part-2.
2) **Function:** Reads a config file containing a list of servers and time intervals, pings each server accordingly, and prints the results to the console.

### Part-4
1) **Library Used:** [`prometheus_client`](https://pypi.org/project/prometheus-client/)
2) **Function:** Records the data captured in Part-3, structures it as metrics, and serves this data through a Prometheus-compatible endpoint.
3) **Prometheus Setup:** Configuration steps to set up Prometheus to scrape the exposed metrics and visualize them as time-series data.
