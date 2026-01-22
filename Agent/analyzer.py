import time
import random
from kubernetes import client, config, watch
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [AI MONITOR] - %(message)s')
logger = logging.getLogger(__name__)

# Heuristic "AI" Model to classify error severity
# In a real V2, this would call an LLM or local model
def classify_error_severity(message):
    critical_keywords = ["CrashLoopBackOff", "OOMKilled", "Error", "Fatal"]
    warning_keywords = ["timeout", "retrying", "slow"]
    
    if any(k in message for k in critical_keywords):
        return "CRITICAL", 0.98  # Severity, Confidence Score
    elif any(k in message for k in warning_keywords):
        return "WARNING", 0.75
    else:
        return "INFO", 0.50

def main():
    try:
        # Load in-cluster configuration (works when running inside K8s)
        try:
            config.load_incluster_config()
            logger.info("Successfully loaded in-cluster configuration.")
        except:
            # Fallback for local testing
            config.load_kube_config()
            logger.info("Loaded local kube-config.")

        v1 = client.CoreV1Api()
        w = watch.Watch()

        logger.info("Starting AI Log Analyzer... Watching for events.")

        # Watch for events in the default namespace
        for event in w.stream(v1.list_namespaced_event, namespace="default"):
            evt_obj = event['object']
            evt_type = evt_obj.type
            evt_message = evt_obj.message
            pod_name = evt_obj.involved_object.name

            # We only care about non-normal events for analysis
            if evt_type != "Normal":
                severity, confidence = classify_error_severity(evt_message)
                
                # Mimic processing time of an AI model
                time.sleep(0.5) 
                
                if severity == "CRITICAL":
                    logger.error(f"🚨 ALERT DETECTED | Pod: {pod_name} | Issue: {evt_message} | Confidence: {confidence}")
                elif severity == "WARNING":
                    logger.warning(f"⚠️ POTENTIAL ISSUE | Pod: {pod_name} | Issue: {evt_message}")

    except Exception as e:
        logger.error(f"Agent crashed: {e}")

if __name__ == "__main__":
    main()