from bareossd import *
from bareos_sd_consts import *

def load_bareos_plugin(context):
  DebugMessage(context, 100, "load_bareos_plugin called\n");
  events = [];
  events.append(bsdEventType['bsdEventJobStart']);
  events.append(bsdEventType['bsdEventJobEnd']);
  RegisterEvents(context, events);
  return bRCs['bRC_OK'];

def handle_plugin_event(context, event):
  if event == bsdEventType['bsdEventJobStart']:
    DebugMessage(context, 100, "bsdEventJobStart event triggered\n");
    jobname = GetValue(context, bsdrVariable['bsdVarJobName']);
    DebugMessage(context, 100, "Job " + jobname + " starting\n");

  elif event == bsdEventType['bsdEventJobEnd']:
    DebugMessage(context, 100, "bsdEventJobEnd event triggered\n");
    jobname = GetValue(context, bsdrVariable['bsdVarJobName']);
    DebugMessage(context, 100, "Job " + jobname + " stopped\n");

  return bRCs['bRC_OK'];

