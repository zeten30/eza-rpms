Name: exa
Version: 0.7.0
Release: 1
Summary: Replacement for 'ls' written in Rust.
Group: Applications/System
BuildRoot: %buildroot
License: MIT
Vendor: Milan Zink <zeten30@gmail.com>
URL: https://github.com/ogham/exa
Packager: Milan Zink <zeten30@gmail.com>
Source0: exa.tar.gz

%description
Replacement for 'ls' written in Rust.

%prep
%setup -q -n exa

%build
# noop

%install
%{__install} -d -m755 %{buildroot}/usr/bin/
%{__cp} -pr exa  %{buildroot}/usr/bin/

%clean
# noop

%files
%defattr(-,root,root,-)
/usr/bin/exa


%changelog
* Tue Sep 12 2017 Milan Zink <zeten30@gmail.com> - 0.7.0-1
- initial exa rpm release
