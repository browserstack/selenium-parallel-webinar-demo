pytest -n 5  parallel/remote_site_tests.py --driver Chrome &  PIDCHROME=$!
pytest -n 5  parallel/remote_site_tests.py --driver Firefox &  PIDFIREFOX=$!
pytest -n 5  parallel/remote_site_tests.py --driver Edge &  PIDEDGE=$!
pytest -n 5  parallel/remote_site_tests.py --driver IE &  PIDIE=$!
pytest -n 5  parallel/remote_site_tests.py --driver Safari &  PIDSAFARI=$!
pytest -n 5  parallel/remote_site_tests.py --driver 'Galaxy S20' &  PIDGALAXY=$!
pytest -n 5  parallel/remote_site_tests.py --driver ios &  PIDSAFARI=$!

wait 