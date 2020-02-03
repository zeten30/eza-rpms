Name: exa
Version: 0.9.2
Release: 2
Summary: Replacement for 'ls' written in Rust.
Group: Applications/System
BuildRoot: %buildroot
License: MIT
Vendor: Benjamin Sago <https://github.com/ogham>
URL: https://github.com/ogham/exa
Packager: Milan Zink <zeten30@gmail.com>
Source0: exa.tar.gz

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description
Replacement for 'ls' written in Rust.

%prep
%setup -q -n exa

%build
# noop

%install
%{__install} -d -m755 %{buildroot}/usr/bin/
%{__cp} -pr exa  %{buildroot}/usr/bin/

%{__install} -d -m755 %{buildroot}/usr/share/man/man1/
%{__cp} -pr exa-man %{buildroot}/usr/share/man/man1/exa.1

%{__install} -d -m755 %{buildroot}/etc/bash_completion.d/
%{__cp} -pr completions.bash %{buildroot}/etc/bash_completion.d/exa

%{__install} -d -m755 %{buildroot}/usr/share/fish/vendor_completions.d/
%{__cp} -pr completions.fish %{buildroot}/usr/share/fish/vendor_completions.d/exa.fish

%{__install} -d -m755 %{buildroot}/usr/share/zsh/vendor-completions/
%{__cp} -pr completions.zsh %{buildroot}/usr/share/zsh/vendor-completions/_exa

%{__install} -d -m755 %{buildroot}/usr/share/licenses/exa/
%{__cp} -pr LICENCE %{buildroot}/usr/share/licenses/exa/LICENCE

%clean
# noop

%files
%license LICENCE
%defattr(-,root,root,-)
/etc/bash_completion.d/exa
/usr/bin/exa
/usr/share/fish/vendor_completions.d/exa.fish
/usr/share/man/man1/exa.1.gz
/usr/share/zsh/vendor-completions/_exa


%changelog
* Fri Jul 26 2019 Milan Zink <zeten30@gmail.com> - 0.9.2-1
- upstream sync

* Tue Mar 27 2018 Milan Zink <zeten30@gmail.com> - 0.9.1-0
- upstream sync (0.9 prerelease)

* Tue Oct 24  2017 Milan Zink <zeten30@gmail.com> - 0.9.0-2
- upstream sync (0.9 prerelease)

* Wed Oct 11 2017 Milan Zink <zeten30@gmail.com> - 0.9.0-1
- upstream sync

* Tue Oct 3 2017 Milan Zink <zeten30@gmail.com> - 0.8.0-1
- upstream sync

* Tue Sep 12 2017 Milan Zink <zeten30@gmail.com> - 0.7.0-3
- completions + man

* Tue Sep 12 2017 Milan Zink <zeten30@gmail.com> - 0.7.0-2
- rpmspec, F27 ready build

* Tue Sep 12 2017 Milan Zink <zeten30@gmail.com> - 0.7.0-1
- initial exa rpm release
