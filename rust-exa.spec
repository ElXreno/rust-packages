%global debug_package %{nil}

%global crate exa

Name:           rust-%{crate}
Version:        0.9.0
Release:        1%{?dist}
Summary:        Modern replacement for ls

License:        MIT
URL:            https://github.com/ogham/exa
Source0:        %{url}/archive/v%{version}/%{crate}-%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

# Fix warning: Could not complete Guile gdb module initialization from:
# /usr/share/gdb/guile/gdb/boot.scm
BuildRequires:  gdb-headless

%description
Modern replacement for ls.


%prep
%autosetup -n %{crate}-%{version}


%build
cargo build --release --locked


%install
cargo install --root=%{buildroot}%{_prefix} --path=. --locked
rm -f %{buildroot}%{_prefix}/.crates.toml %{buildroot}%{_prefix}/.crates2.json


%files
%doc README.md
%license LICENCE
%{_bindir}/%{crate}



%changelog
* Mon Mar 16 2020 ElXreno <elxreno@gmail.com>
- Initial packaging
