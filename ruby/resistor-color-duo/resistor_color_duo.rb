class ResistorColorDuo
  def self.value arr
    colors = [ "black","brown","red","orange","yellow","green","blue","violet","grey","white", ]
    rtv = ""
    arr.each do |color|
      break if 1 < rtv.length
      rtv += colors.index(color).to_s
    end
    rtv.to_i
  end
end