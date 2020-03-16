%global crate fd

Name:           rust-%{crate}
Version:        7.4.0
Release:        1%{?dist}
Summary:        Fd is a simple, fast and user-friendly alternative to find

License:        MIT or ASL 2.0
URL:            https://github.com/sharkdp/fd
Source0:        %{url}/archive/v%{version}/%{crate}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

# Fix warning: Could not complete Guile gdb module initialization from:
# /usr/share/gdb/guile/gdb/boot.scm
BuildRequires:  gdb-headless

%description
Fd is a simple, fast and user-friendly alternative to find.


%prep
%autosetup -n %{crate}-%{version}


%build
cargo build --release --locked


%install
cargo install --root=%{buildroot}%{_prefix} --path=. --locked
rm -f %{buildroot}%{_prefix}/.crates.toml %{buildroot}%{_prefix}/.crates2.json


%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{crate}



%changelog
* Mon Mar 16 2020 ElXreno <elxreno@gmail.com>
- Initial packaging
