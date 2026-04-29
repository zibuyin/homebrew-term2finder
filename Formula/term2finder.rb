class Term2finder < Formula
  desc "Open Finder from the terminal with file reveal and view controls"
  homepage "https://github.com/zibuyin/term2finder"
  url "https://github.com/zibuyin/term2finder/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "REPLACE_WITH_SOURCE_TARBALL_SHA256"
  license "MIT"

  depends_on :macos

  def install
    bin.install "tf.py" => "tf"
  end

  test do
    assert_match "usage", shell_output("#{bin}/tf -h")  
  end
end
