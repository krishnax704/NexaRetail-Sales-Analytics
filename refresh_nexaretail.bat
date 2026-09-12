@echo off
cd /d "%~dp0"

echo ==========================================
echo NexaRetail ETL Started
echo ==========================================

python sales_analytics_pipeline_automated.py

echo.
echo ==========================================
echo NexaRetail ETL Finished
echo ==========================================
