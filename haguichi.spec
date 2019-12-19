Name:           haguchi
Version:        1.4.2
Release:        1
Summary:        Hamachi Network Manager
License:        GPLv3+
Group:          Productivity/Networking/Other
URL:            https://www.haguichi.net/
Source0:        https://github.com/ztefn/haguichi/releases/download/%{version}/%{name}-%{version}.tar.xz
# Mirror source: https://launchpad.net/haguichi/s
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang
