<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Identity transform: copies all elements and attributes -->
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <!-- Add <test>in</test> inside the <child> element -->
    <xsl:template match="/catalog/cd">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
            <test>sample</test>
        </xsl:copy>
    </xsl:template>

</xsl:stylesheet>
