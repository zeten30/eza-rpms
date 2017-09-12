# RPM Makefile
RELEASE=26

sources:
	./sources.sh

clean:
	rm -rf rpmbuild/*.*
	rm -rf src/*.tar.gz

srpm: clean sources
	mock -r fedora-$(RELEASE)-x86_64 --spec exa.spec --sources src/ --resultdir rpmbuild/ --buildsrpm


rpm: srpm
	mock -r fedora-$(RELEASE)-x86_64 --rebuild rpmbuild/exa-*.src.rpm --resultdir rpmbuild/


copr: srpm
	copr-cli build mzink/Utils rpmbuild/exa-*.src.rpm --nowait
