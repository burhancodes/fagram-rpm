Name:           fagram
Version:        2.1.4
Release:        1%{?dist}
Summary:        FAgram Desktop is a custom Telegram client.
Vendor:         burhancodes
Group:          Applications/Internet
Packager:       Burhanverse  <contact@burhanverse.eu.org>
License:        GPLv3
URL:            https://github.com/burhancodes/fagramdesktop
Source0:        https://github.com/burhancodes/fagram-rpm/releases/download/v%{version}/fagram-%{version}.tar.gz

%description
FAgram Desktop is a custom Telegram client.

Author: FajoX1  <FajoX1@github.com>

%prep
tar -xvf %{_sourcedir}/fagram-%{version}.tar.gz -C %{_sourcedir}
cd %{_sourcedir}/

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/dbus-1
mkdir -p %{buildroot}/usr/share/icons
mkdir -p %{buildroot}/usr/share/metainfo

cp -a %{_sourcedir}/usr/bin/fagram %{buildroot}/usr/bin/

cp -a %{_sourcedir}/usr/share/* %{buildroot}/usr/share/

%files
/usr/bin/fagram
%dir /usr/share/applications
/usr/share/applications/*
%dir /usr/share/dbus-1
/usr/share/dbus-1/*
%dir /usr/share/icons
/usr/share/icons/*
%dir /usr/share/metainfo
/usr/share/metainfo/*

%post
if [ -f "/usr/share/applications/org.fagram.desktop.desktop" ]; then
  rm -f /usr/share/applications/org.fagram.desktop.desktop
fi

%preun
  pkill -f '/usr/bin/fagram' || true

%postun
if [ "$1" -eq 0 ]; then
  USER_HOME="/home/${SUDO_USER:-$USER}"

  if [ -d "$USER_HOME/.local/share/FAgramDesktop" ]; then
    rm -rf "$USER_HOME/.local/share/FAgramDesktop"
  fi
fi
