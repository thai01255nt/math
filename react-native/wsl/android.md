sudo apt install unzip
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip -d Android
rm platform-tools-latest-linux.zip
sudo apt install -y lib32z1 openjdk-8-jrk
set -gx JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
set -gx PATH $JAVA_HOME/bin $PATH
cd /Android/tools/bin
sdkmanager "platform-tools" \
 "platforms;android-35" \
 "build-tools;35.0.0" \
 "system-images;android-35;google_apis;x86_64" \
 "system-images;android-35;google_apis;x86_64" \
 "ndk-bundle" \
 "ndk;26.1.10909125"
set -gx ANDROID_HOME ~/Android/
set -gx PATH $ANDROID_HOME/tools
set -gx PATH $ANDROID_HOME/platform-tools
android update sdk --no-ui
sudo apt-get install gradle
gradle -v

unzip and copy cmdline-tools into android_sdk
cd and ./sdkmanager with --sdk_root=/home/<>/android_sdk (for install or license purpose)
set -gx ANDROID_HOME ~/android_sdk
set -gx PATH $ANDROID_HOME/bin $PATH
set -gx PATH $ANDROID_HOME/lib $PATH
