# RPM Makefile
RELEASE=38

sources:
	./sources.sh

clean:
	rm -rf rpmbuild/*.*
	rm -rf src/*.tar.gz
	rm -rf src/eza/completions
	rm -rf src/eza/eza
	rm -rf src/eza/LICEN*E

srpm: clean sources
	mock -r fedora-$(RELEASE)-x86_64 --spec eza.spec --sources src/ --resultdir rpmbuild/ --buildsrpm


rpm: srpm
	mock -r fedora-$(RELEASE)-x86_64 --rebuild rpmbuild/eza-*.src.rpm --resultdir rpmbuild/


copr: srpm
	copr-cli build mzink/Utils rpmbuild/eza-*.src.rpm --nowait
