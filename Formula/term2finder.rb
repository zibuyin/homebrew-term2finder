class Term2finder < Formula
  desc "Open Finder from the terminal with file reveal and view controls"
  homepage "https://github.com/zibuyin/term2finder"
  url "https://github.com/zibuyin/term2finder/archive/refs/tags/v1.0.1.tar.gz"
  sha256 "57d03d7e6448b0c65419091d6bc77a3d0635fe3085008dd94e6625905f80d98d"
  license "MIT"

  depends_on :macos

  def install
    bin.install "tf.py" => "tf"
  end

  test do
    assert_match "usage", shell_output("#{bin}/tf -h")  
  end
end
