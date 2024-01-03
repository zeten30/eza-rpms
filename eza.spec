Name: eza
Version: 0.17.0
Release: 1
Summary: Replacement for 'ls' written in Rust.
Group: Applications/System
BuildRoot: %buildroot
License: MIT
Vendor: Christina Sørensen <https://github.com/cafkafk>
URL: https://github.com/eza-community/eza

Source0: eza.tar.gz

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description
Replacement for 'ls' written in Rust.

%prep
%setup -q -n eza

%build
# noop

%install
%{__install} -d -m755 %{buildroot}/usr/bin/
%{__cp} -pr eza  %{buildroot}/usr/bin/

%{__install} -d -m755 %{buildroot}/etc/bash_completion.d/
%{__cp} -pr completions/bash/eza %{buildroot}/etc/bash_completion.d/eza

%{__install} -d -m755 %{buildroot}/usr/share/fish/vendor_completions.d/
%{__cp} -pr completions/fish/eza.fish %{buildroot}/usr/share/fish/vendor_completions.d/eza.fish

%{__install} -d -m755 %{buildroot}/usr/share/zsh/vendor-completions/
%{__cp} -pr completions/zsh/_eza %{buildroot}/usr/share/zsh/vendor-completions/_eza

%{__install} -d -m755 %{buildroot}/usr/share/licenses/eza/
%{__cp} -pr LICENSE %{buildroot}/usr/share/licenses/eza/LICENSE

%files
%license LICENSE
%defattr(-,root,root,-)
/etc/bash_completion.d/eza
/usr/bin/eza
/usr/share/fish/vendor_completions.d/eza.fish
/usr/share/zsh/vendor-completions/_eza


%changelog
* Wed Jan 3 2024 Milan Zink <zeten30@gmail.com> - 0.17.0.1
- new upstream release

* Wed Sep 13 2023 Milan Zink <zeten30@gmail.com> - 0.11.2.1
- exa forked and renamed to eza

* Fri Jul 26 2019 Milan Zink <zeten30@gmail.com> - 0.9.2-1
- upstream sync

* Tue Mar 27 2018 Milan Zink <zeten30@gmail.com> - 0.9.1-0
- upstream sync (0.9 prerelease)
