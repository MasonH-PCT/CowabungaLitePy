import tools.status_bar.status_setter15 as status_setter15
import tools.status_bar.status_setter16 as status_setter16
import tools.status_bar.status_setter16_1 as status_setter16_1
from devicemanagement.constants import Version

class StatusSetter:
    def __init__(self, version: str, workspace: str):
        parsed_ver: Version = Version(version)
        if parsed_ver >= Version("16.1"):
            self.setter = status_setter16_1.Setter(workspace)
        elif parsed_ver >= Version("16.0"):
            self.setter = status_setter16.Setter(workspace)
        else:
            self.setter = status_setter15.Setter(workspace)

        
    ### PRIMARY CARRIER
    # CELLULAR SERVICE
    def is_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def get_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def set_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideServiceString == 1
    def get_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.serviceString.decode()
    def set_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 1
        # TODO: Truncate strings
        overrides.values.serviceString = text.encode()
        overrides.values.serviceCrossfadeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_primary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overridePrimaryServiceBadgeString == 1
    def get_primary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.primaryServiceBadgeString.decode()
    def set_primary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 1
        overrides.values.primaryServiceBadgeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_primary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDataNetworkType == 1
    def get_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.dataNetworkType
    def set_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 1
        overrides.values.dataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideGSMSignalStrengthBars == 1
    def get_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.GSMSignalStrengthBars
    def set_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideGSMSignalStrengthBars = 1
        overrides.values.GSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### SECONDARY CARRIER
    # CELLULAR SERVICE
    def is_secondary_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def get_secondary_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def set_secondary_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1 if shown else 0
        overrides.overrideSecondaryCellularConfigured = 1
        overrides.values.secondaryCellularConfigured = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_secondary_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 0
        overrides.overrideSecondaryCellularConfigured = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_secondary_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceString == 1
    def get_secondary_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryServiceString.decode()
    def set_secondary_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 1
        overrides.values.secondaryServiceString = text.encode()
        overrides.values.secondaryServiceCrossfadeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_secondary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceBadgeString == 1
    def get_secondary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryServiceBadgeString.decode()
    def set_secondary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 1
        overrides.values.secondaryServiceBadgeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_secondary_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryDataNetworkType == 1
    def get_secondary_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryDataNetworkType
    def set_secondary_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 1
        overrides.values.secondaryDataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_secondary_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_secondary_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryGSMSignalStrengthBars == 1
    def get_secondary_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryGSMSignalStrengthBars
    def set_secondary_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideSecondaryGSMSignalStrengthBars = 1
        overrides.values.secondaryGSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_secondary_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideSecondaryGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### MISC TEXT INPUTS
    # DATE STRING (Unused)
    def is_date_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDateString == 1
    def get_date_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.dateString.decode()
    def set_date(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 1
        overrides.values.dateString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_date(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 0
        self.setter.apply_changes(overrides)

    # TIME STRING
    def is_time_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideTimeString == 1
    def get_time_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.timeString.decode()
    def set_time(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 1
        overrides.values.timeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_time(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 0
        self.setter.apply_changes(overrides)

    # BREADCRUMB STRING
    def is_crumb_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBreadcrumb == 1
    def get_crumb_override(self) -> str:
        overrides = self.setter.get_overrides()
        text: str = overrides.values.breadcrumbTitle.decode()
        if len(text) > 1:
            return text[:len(text) - 4]
        return ""
    def set_crumb(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 1
        new_crumb = ""
        if text != "":
            new_crumb: str = text + " ▶"
        overrides.values.breadcrumbTitle = new_crumb.encode()
        self.setter.apply_changes(overrides)
    def unset_crumb(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 0
        overrides.values.breadcrumbTitle = "".encode()
        self.setter.apply_changes(overrides)

    # BATTERY DETAIL STRING
    def is_battery_detail_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBatteryDetailString == 1
    def get_battery_detail_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.batteryDetailString.decode()
    def set_battery_detail(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 1
        overrides.values.batteryDetailString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_battery_detail(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 0
        self.setter.apply_changes(overrides)


    ## MISC SLIDER INPUTS
    # BATTERY CAPACITY
    def is_battery_capacity_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBatteryCapacity == 1
    def get_battery_capacity_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.batteryCapacity
    def set_battery_capacity(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryCapacity = 1
        overrides.values.batteryCapacity = id
        self.setter.apply_changes(overrides)
    def unset_battery_capacity(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryCapacity = 0
        self.setter.apply_changes(overrides)

    # WIFI SIGNAL STRENGTH
    def is_wifi_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideWifiSignalStrengthBars == 1
    def get_wifi_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.wifiSignalStrengthBars
    def set_wifi_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideWifiSignalStrengthBars = 1
        overrides.values.wifiSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_wifi_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideWifiSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ## RAW SIGNAL STRENGTH TOGGLES
    # WIFI
    def is_raw_wifi_signal_shown(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDisplayRawWifiSignal == 1
    def show_raw_wifi_signal(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        if shown:
            overrides.overrideDisplayRawWifiSignal = 1
            overrides.values.displayRawWiFiSignal = 1
        else:
            overrides.overrideDisplayRawWifiSignal = 0
        self.setter.apply_changes(overrides)
    # GSM
    def is_raw_gsm_signal_shown(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDisplayRawGSMSignal == 1
    def show_raw_gsm_signal(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        if shown:
            overrides.overrideDisplayRawGSMSignal = 1
            overrides.values.displayRawGSMSignal = 1
        else:
            overrides.overrideDisplayRawGSMSignal = 0
        self.setter.apply_changes(overrides)


    ## HIDE OPTION TOGGLES
    # DND
    def is_dnd_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.QuietModeStatusBarItem.value] == 1
    def hide_dnd(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.QuietModeStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.QuietModeStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.QuietModeStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # AIRPLANE
    def is_airplane_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirplaneModeStatusBarItem.value] == 1
    def hide_airplane(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirplaneModeStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.AirplaneModeStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirplaneModeStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # CELL
    def is_cell_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def hide_cell(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # WIFI
    def is_wifi_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularDataNetworkStatusBarItem.value] == 1
    def hide_wifi(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularDataNetworkStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularDataNetworkStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularDataNetworkStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # BATTERY
    def is_battery_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.MainBatteryStatusBarItem.value] == 1
    def hide_battery(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.MainBatteryStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.MainBatteryStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.MainBatteryStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # BLUETOOTH
    def is_bluetooth_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.BluetoothStatusBarItem.value] == 1
    def hide_bluetooth(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.BluetoothStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.BluetoothStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.BluetoothStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # ALARM
    def is_alarm_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AlarmStatusBarItem.value] == 1
    def hide_alarm(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AlarmStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.AlarmStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AlarmStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # LOCATION
    def is_location_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.LocationStatusBarItem.value] == 1
    def hide_location(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.LocationStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.LocationStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.LocationStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # ROTATION LOCK
    def is_rotation_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.RotationLockStatusBarItem.value] == 1
    def hide_rotation(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.RotationLockStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.RotationLockStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.RotationLockStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # AIRPLAY
    def is_airplay_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirPlayStatusBarItem.value] == 1
    def hide_airplay(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirPlayStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.AirPlayStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.AirPlayStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # CARPLAY
    def is_carplay_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CarPlayStatusBarItem.value] == 1
    def hide_carplay(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CarPlayStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.CarPlayStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CarPlayStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
    # VPN
    def is_vpn_hidden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.VPNStatusBarItem.value] == 1
    def hide_vpn(self, hidden: bool) -> None:
        overrides = self.setter.get_overrides()
        if hidden:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.VPNStatusBarItem.value] = 1
            overrides.values.itemIsEnabled[self.setter.StatusBarItem.VPNStatusBarItem.value] = 0
        else:
            overrides.overrideItemIsEnabled[self.setter.StatusBarItem.VPNStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
