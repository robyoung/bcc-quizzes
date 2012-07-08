import boto

conn = boto.connect_ec2()

urls = open("urls.txt", "w+")

for reservation in conn.get_all_instances():
  for instance in reservation.instances:
    if instance.state == "running" and instance.tags.get("usage") == "ipython":
      urls.write("%s\n" % instance.public_dns_name)