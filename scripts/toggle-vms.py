import boto

conn = boto.connect_ec2()

for reservation in conn.get_all_instances():
  for instance in reservation.instances:
    if instance.tags.get("bcc") == "true":
      print instance,
      if instance.state == "running":
        instance.stop()
        print("stopped")
      elif instance.state == "stopped":
        instance.start()
        print("started")
      else:
        print("currently %s" % instance.state)