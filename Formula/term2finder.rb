class Term2finder < Formula
  desc "Open Finder from the terminal with file reveal and view controls"
  homepage "https://github.com/zibuyin/term2finder"
  url "https://github.com/zibuyin/homebrew-term2finder/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "053dcc5f039f418f6373088162fe341f0449f2e69695c6e494bb69d59d75ac9b"
  license "MIT"

  depends_on :macos

  def install
    bin.install "tf" => "tf"
  end

  test do
    assert_match "usage", shell_output("#{bin}/tf -h")  
  end
end
