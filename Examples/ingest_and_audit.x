## Perform test
U fetch reddit /r/machinelearning count=500
U normalize
U transform method=shorthand_v1
U audit checks=toxicity,coherence
U export audit=audits/audit_run.xlog
