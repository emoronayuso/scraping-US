from crontab import CronTab

#####################################################
### MORE info about python-crontab ##################
### https://pypi.python.org/pypi/python-crontab #####
#####################################################

root_directory = '/home/kike/scraping-US/spider-ENI-SOLFA/'

tab = CronTab(user='root')

cmd_scrapy = 'python '+root_directory+'cron_job/run_spider.py >/dev/null 2>&1'
cmd_graphs = 'python '+root_directory+'graphs/general.py >/dev/null 2>&1'
cmd_html = 'python '+root_directory+'html/generate_html.py >/dev/null 2>&1'

############# ADD CRON JOB ##################
cron_scrapy = tab.new(cmd_scrapy)
cron_graphs = tab.new(cmd_graphs)
cron_html = tab.new(cmd_html)

#Job every 7 days to 1 am
cron_scrapy.setall("0 1 */7 * *")
cron_graphs.setall("0 4 */7 * *")
cron_html.setall("5 4 */7 * *")

#cron_html.minute.every(8)

#WRITE CRON JOB
tab.write()

##SHOW NEW CRON JOB
print tab.render()
##############################################

## DEL CRON JOB#############
#cron_job = tab.find_command(cmd_graphs)
#cron_job2 = tab.find_command(cmd_scrapy)
#cron_job3 = tab.find_command(cmd_html)

#tab.remove_all(cmd_graphs)
#tab.remove_all(cmd_scrapy)
#tab.remove_all(cmd_html)

#Write content crontab
#tab.write()

#print tab.render()
####################################

